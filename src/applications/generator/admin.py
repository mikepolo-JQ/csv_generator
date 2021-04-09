from django.contrib import admin

from applications.generator.models import Schema, Column


@admin.register(Schema)
class SchemaAdminModel(admin.ModelAdmin):
    pass


@admin.register(Column)
class ColumnAdminModel(admin.ModelAdmin):
    pass
