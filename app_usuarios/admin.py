from django.contrib import admin
from django.utils.html import format_html
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .forms import UserProfileForm

# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    form = UserProfileForm

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if change:
            try:
                profile = obj.userprofile
            except UserProfile.DoesNotExist:
                profile = UserProfile(user=obj)
            profile.save()

admin.site.unregister(User)
admin.site.register(User, UserAdmin)