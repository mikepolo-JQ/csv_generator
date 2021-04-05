from django.apps import AppConfig


class GeneratorConfig(AppConfig):
    lable = "generator"
    name = f"applications.{lable}"
