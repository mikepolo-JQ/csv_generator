from django.views.generic import ListView
from django.views.generic import TemplateView

from applications.generator.models import Schema


class IndexView(TemplateView):
    template_name = "landing/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        user = self.request.user
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
