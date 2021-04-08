from django.urls import path

from applications.landing.apps import LandingConfig
from applications.landing.views import IndexView, DataSetView

app_name = LandingConfig.lable

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("dataset/", DataSetView.as_view(), name="dataset")

]
