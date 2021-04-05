from django.urls import path

from applications.generator.views import CreateView

urlpatterns = [
    path("", CreateView.as_view(), name="create"),
]
