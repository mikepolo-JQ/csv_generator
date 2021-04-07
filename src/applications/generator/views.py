import json
from cgi import parse_multipart, parse
from urllib.parse import parse_qs

from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView


class CreateView(TemplateView):
    template_name = "generator/create.html"


class GeneratorView(View):
    def post(self, request, *args, **kwargs):

        body = request.environ.get("wsgi.input")
        length = int(request.environ.get("CONTENT_LENGTH") or 0)

        if not length:
            return b""

        content = body.read(length).decode()

        b = json.loads(content)

        print(b)

        payload = {"ok": True, "data": None}
        return JsonResponse(payload)

