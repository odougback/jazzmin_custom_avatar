from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assinatura = models.ImageField(upload_to='assinaturas/', blank=True, null=True)
    profile_picture = models.ImageField(upload_to='foto_perfil/', blank=True, null=True, verbose_name="foto de perfil")

    class Meta:
        verbose_name = "informação extra"
        verbose_name_plural = "informações extras"

    def __str__(self):
        return self.user.username

@receiver(pre_save, sender=UserProfile)
def delete_old_assinatura(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).assinatura
    except sender.DoesNotExist:
        return False

    new_file = instance.assinatura
    if old_file and old_file != new_file:
        old_file.delete(save=False)

@receiver(pre_delete, sender=UserProfile)
def delete_assinatura_on_delete(sender, instance, **kwargs):
    if instance.assinatura:
        instance.assinatura.delete(save=False)
