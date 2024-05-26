from django import template
from django.templatetags.static import static
from app_usuarios.models import UserProfile

register = template.Library()

@register.simple_tag
def get_user_profile_picture(user):
    try:
        profile = UserProfile.objects.get(user=user)
        if profile.profile_picture:
            return profile.profile_picture.url
        else:
            return static('img/avatar.png')  # Substitua pelo caminho da imagem padrão
    except UserProfile.DoesNotExist:
        return static('img/avatar.png')  # Substitua pelo caminho da imagem padrão
