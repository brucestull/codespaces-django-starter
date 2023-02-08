from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Need to determine best practice for importing models:
# Use `accounts.forms` or `.forms`?
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Custom user admin. This class extends `UserAdmin`.

    This class modifies the default `UserAdmin` to use custom forms and
    control displayed fields in Django Admin.
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "id",
        "email",
        "username",
    ]
