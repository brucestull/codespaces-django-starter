from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from accounts.forms import CustomUserCreationForm


class SignUpView(CreateView):
    """
    View for signing up a new user.
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
