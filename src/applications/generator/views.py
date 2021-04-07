import json
import csv
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

from applications.generator.utils import get_data, get_columns_values


class CreateView(TemplateView):
    template_name = "generator/create.html"


class GeneratorView(View):
    def post(self, request, *args, **kwargs):

        data = get_data(request.environ)

        filename = data['name'] + ".csv"
        char = data['char']
        sep = data['sep']
        columns = data['columns']
        columns.sort(key=lambda i: i['order'])

        rows = get_columns_values(columns)

        with open(filename, 'w', newline='') as fp:
            fieldnames = []

            for column in columns:
                fieldnames.append(column["name"])

            writer = csv.DictWriter(fp, delimiter=sep, quotechar=char, fieldnames=fieldnames)

            writer.writeheader()

            for row in rows:
                writer.writerow(row)

        payload = {"ok": True, "data": None}
        return JsonResponse(payload)

