from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture',]  # Corrija aqui se estiver usando 'foto_de_perfil'
