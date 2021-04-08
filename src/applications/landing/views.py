import os

import boto3
from django.conf import settings
from django.http import JsonResponse
from django.views import View
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


class DownloadView(View):
    def post(self, request, *args, **kwargs):
        BUCKET_NAME = settings.AWS_STORAGE_BUCKET_NAME
        env = os.environ
        print(env)
        s3 = boto3.client('s3',
                          aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
        s3.download_file(BUCKET_NAME, 'mediawelcom_to_AWS.csv', 'D:/downAWS/test_AWS.csv')
        payload = {"ok": True, "data": None}

        return JsonResponse(payload)
