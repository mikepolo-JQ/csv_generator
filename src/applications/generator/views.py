
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from applications.generator.tasks import celery_generator_csv
from applications.generator.utils import get_data


class CreateView(TemplateView):
    template_name = "generator/create.html"


class GeneratorView(View):
    def post(self, request, *args, **kwargs):
        data = get_data(request.environ)

        celery_generator_csv.delay(data)

        payload = {"ok": True, "data": None}
        return JsonResponse(payload)
