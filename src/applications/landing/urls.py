from django.urls import path

from applications.landing.apps import LandingConfig
from applications.landing.views import IndexView

app_name = LandingConfig.lable

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
