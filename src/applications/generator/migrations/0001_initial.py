# Generated by Django 3.2 on 2021-04-09 00:19

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Schema",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="noname_schema", max_length=50)),
                ("sep", models.CharField(default=",", max_length=10)),
                ("char", models.CharField(default='"', max_length=50)),
                ("status", models.BooleanField(default=False)),
                ("modified", models.DateTimeField(default=datetime.datetime.now)),
                ("filename", models.CharField(default="", max_length=50)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="schemas",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Column",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="noname_column", max_length=50)),
                ("columntype", models.CharField(default="", max_length=50)),
                ("intfrom", models.IntegerField(default=1)),
                ("intto", models.IntegerField(default=100)),
                ("order", models.IntegerField(default=0)),
                (
                    "schema",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="columns",
                        to="generator.schema",
                    ),
                ),
            ],
        ),
    ]
