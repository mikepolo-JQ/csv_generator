from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Schema(models.Model):
    author = models.ForeignKey(User, related_name="schemas", on_delete=models.CASCADE)
    name = models.CharField(
        null=False, blank=False, max_length=50, default="noname_schema"
    )
    sep = models.CharField(null=False, blank=False, max_length=10, default=",")
    char = models.CharField(null=False, blank=False, max_length=50, default='"')

    filename = models.FileField()

    def __str__(self):
        return f"{self.name}"


class Column(models.Model):
    name = models.CharField(
        null=False, blank=False, max_length=50, default="noname_column"
    )
    columntype = models.CharField(null=False, blank=False, max_length=50, default="")
    intfrom = models.IntegerField(default=1)
    intto = models.IntegerField(default=100)
    schema = models.ForeignKey(Schema, related_name="columns", on_delete=models.CASCADE)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"
