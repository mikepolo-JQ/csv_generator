from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from applications.generator.apps import GeneratorConfig
from applications.generator.views import CreateView
from applications.generator.views import GeneratorView

app_name = GeneratorConfig.lable

urlpatterns = [
    path("", CreateView.as_view(), name="create"),
    path("s/", csrf_exempt(GeneratorView.as_view()), name="generator"),
]
