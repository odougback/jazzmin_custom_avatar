from django.db.models.signals import pre_save, pre_delete, post_save
from django.dispatch import receiver
from .models import UserProfile
from django.contrib.auth.models import User

@receiver(pre_save, sender=UserProfile)
def delete_old_files(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_profile = sender.objects.get(pk=instance.pk)
        old_assinatura = old_profile.assinatura
        old_profile_picture = old_profile.profile_picture
    except sender.DoesNotExist:
        return False

    new_assinatura = instance.assinatura
    if old_assinatura and old_assinatura != new_assinatura:
        old_assinatura.delete(save=False)

    new_profile_picture = instance.profile_picture
    if old_profile_picture and old_profile_picture != new_profile_picture:
        old_profile_picture.delete(save=False)

@receiver(pre_delete, sender=UserProfile)
def delete_files_on_delete(sender, instance, **kwargs):
    if instance.assinatura:
        instance.assinatura.delete(save=False)
    if instance.profile_picture:
        instance.profile_picture.delete(save=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
