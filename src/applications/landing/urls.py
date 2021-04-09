from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from applications.landing.apps import LandingConfig
from applications.landing.views import DataSetView
from applications.landing.views import IndexView
from applications.landing.views import StartStatusView

app_name = LandingConfig.lable

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("dataset/", DataSetView.as_view(), name="dataset"),
    path("startstatus/", csrf_exempt(StartStatusView.as_view()), name="ss"),
]
