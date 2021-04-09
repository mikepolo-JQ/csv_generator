
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from applications.generator.models import Schema


class IndexView(TemplateView):
    template_name = "landing/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        user = self.request.user

        if not user.is_authenticated:
            schemas = Schema.objects.all().first()
            context.update({"redirect": True})
            return context
        else:
            schemas = Schema.objects.filter(author=user)

        context.update({"schemas": schemas})
        return context


class DataSetView(TemplateView):
    template_name = "landing/dataset.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        user = self.request.user
        schemas = Schema.objects.filter(author=user)
        context.update({"schemas": schemas})
        return context


class StartStatusView(View):
    def post(self, request, *args, **kwargs):

        user = self.request.user
        schemas = Schema.objects.filter(author=user)
        pks = []
        for schema in schemas:
            if not schema.status:
                continue
            pks.append(schema.pk)

        payload = {"ok": True, "data": pks}
        return JsonResponse(payload)
