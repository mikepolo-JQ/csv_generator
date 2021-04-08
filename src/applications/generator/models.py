from django.db import models

#
#
# class Schema(models.Model):
#     name = models.CharField(null=False, blank=False, max_length=50, default="noname_schema")
#     sep = models.CharField(null=False, blank=False, max_length=10, default=",")
#     character = models.CharField(null=False, blank=False, max_length=50, default="\"")
#
#     filename = models.FileField()
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class Column(models.Model):
#     name = models.CharField(null=False, blank=False, max_length=50, default="noname_column")
#     columntype = models.CharField(null=False, blank=False, max_length=50, default="")
#     schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.name}"
