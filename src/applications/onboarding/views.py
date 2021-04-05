from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


class SignInView(LoginView):
    template_name = "onboarding/sign-in.html"


class SignOutView(LogoutView):
    template_name = "onboarding/signed-out.html"
