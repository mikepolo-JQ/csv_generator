from django.views.generic import TemplateView


class CreateView(TemplateView):
    template_name = "generator/create.html"
