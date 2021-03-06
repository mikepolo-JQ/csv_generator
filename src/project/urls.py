from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", include("applications.landing.urls"), name="landing"),
    path("o/", include("applications.onboarding.urls"), name="onboarding"),
    path("g/", include("applications.generator.urls"), name="generator"),
]
