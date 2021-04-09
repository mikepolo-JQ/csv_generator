import csv

from celery import shared_task
from django.conf import settings

from applications.generator.models import Schema
from applications.generator.utils import get_columns_data
from applications.generator.utils import get_rows
from applications.generator.utils import upload_file


@shared_task
def celery_generator_csv(user_id, rows_count):
    schemas = Schema.objects.filter(author_id=user_id)

    for schema in schemas:
        filename = schema.filename
        char = schema.char
        sep = schema.sep
        columns = get_columns_data(schema.pk)
        columns.sort(key=lambda i: i["order"])

        rows = get_rows(columns, rows_count)

        with open(filename, "w", newline="") as fp:
            fieldnames = []

            for column in columns:
                fieldnames.append(column["name"])

            writer = csv.DictWriter(
                fp, delimiter=sep, quotechar=char, fieldnames=fieldnames
            )

            writer.writeheader()
            for row in rows:
                writer.writerow(row)

        res = upload_file(file_name=filename)

        if res:
            schema.status = True
            schema.save()
