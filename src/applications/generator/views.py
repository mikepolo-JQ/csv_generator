from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView
from django.views.generic import FormView
from django.views.generic import TemplateView

from applications.generator.models import Schema
from applications.generator.tasks import celery_generator_csv
from applications.generator.utils import create_models
from applications.generator.utils import get_data


class CreateView(TemplateView):
    template_name = "generator/create.html"


class SchemasGeneratorView(View):
    def post(self, request, *args, **kwargs):
        data = get_data(request.environ)
        user = self.request.user

        create_models(data, user)

        payload = {"ok": True, "data": None}
        return JsonResponse(payload)


class CSVGeneratorView(View):
    def post(self, request, *args, **kwargs):
        user_id = self.request.user.id
        rows = kwargs["rows"]

        celery_generator_csv.delay(user_id, rows)

        payload = {"ok": True, "data": None}
        return JsonResponse(payload)


class DeleteSchemaView(DeleteView):
    http_method_names = ["post"]
    model = Schema
    success_url = reverse_lazy("landing:index")


class EditSchemaView(TemplateView):
    template_name = "generator/edit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        pk = kwargs["pk"] or 0

        if not pk:
            raise ModuleNotFoundError(f"Schema with pk={pk} isn't found")

        schema = Schema.objects.filter(pk=pk).first()
        countplusone = schema.columns.all().count() + 1
        context.update({"schema": schema, "countplusone": countplusone})
        return context
