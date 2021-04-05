from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = (
            "password1",
            "password2",
            "username",
        )
