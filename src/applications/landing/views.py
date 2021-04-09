import os

import boto3
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView
from django.views.generic import TemplateView

from applications.generator.models import Schema
from applications.landing.tasks import celery_file_download


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


class DownloadView(View):
    def post(self, request, *args, **kwargs):

        pk = kwargs["pk"]
        filename = Schema.objects.filter(pk=pk).first().filename

        celery_file_download.delay(filename)

        payload = {"ok": True, "data": None}

        return JsonResponse(payload)


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
