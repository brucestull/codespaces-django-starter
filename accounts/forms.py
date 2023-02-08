from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    Form for creating a new user. This class extends `UserCreationForm`.
    """

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
        )

class CustomUserChangeForm(UserChangeForm):
    """
    Form for updating a user. This class extends `UserChangeForm`.
    """

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
        )
