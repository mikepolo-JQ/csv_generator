from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from applications.generator.apps import GeneratorConfig
from applications.generator.views import CreateView
from applications.generator.views import CSVGeneratorView
from applications.generator.views import DeleteSchemaView
from applications.generator.views import EditSchemaView
from applications.generator.views import SchemasGeneratorView

app_name = GeneratorConfig.lable

urlpatterns = [
    path("", CreateView.as_view(), name="create"),
    path("s/", csrf_exempt(SchemasGeneratorView.as_view()), name="generator"),
    path("s/<int:rows>/csv/", csrf_exempt(CSVGeneratorView.as_view()), name="csv"),
    path("s/<int:pk>/delete/", csrf_exempt(DeleteSchemaView.as_view()), name="delete"),
    path("s/<int:pk>/edit/", EditSchemaView.as_view(), name="edit"),
]
