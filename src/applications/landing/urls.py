from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from applications.landing.apps import LandingConfig
from applications.landing.views import IndexView, DataSetView, DownloadView

app_name = LandingConfig.lable

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("dataset/", DataSetView.as_view(), name="dataset"),
    path("download/", csrf_exempt(DownloadView.as_view()), name="download")

]
