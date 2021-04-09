import json
import logging
import random

import boto3
from botocore.exceptions import ClientError
from django.conf import settings

from applications.generator.models import Column
from applications.generator.models import Schema


def get_data(environ):
    body = environ.get("wsgi.input")
    length = int(environ.get("CONTENT_LENGTH") or 0)

    if not length:
        raise ValueError("Server didn't receive the data.")

    content = body.read(length).decode()
    data = json.loads(content)

    return data


column_values = {
    "int": False,
    "job": ["Developer", "Teacher", "Driver", "Artist", "Astronaut"],
    "name": [
        "Johnny Depp",
        "Al Pacino",
        "Robert De Niro",
        "Kevin Spacey",
        "Denzel Washington",
    ],
    "company": ["Google", "Coca-cola", "Nike", "Adidas", "Ebay"],
    "date": ["2020.01.03", "2015.06.14", "2010.04.23", "2017.05.07", "2021.04.08"],
}


def get_rows(columns, rows_count) -> list:
    result = []
    column_dict = {}

    for i in range(rows_count):
        for column in columns:
            list_value = column_values[column["type"]]

            if not list_value:
                value = random.randint(int(column["from"]), int(column["to"]))
            else:
                value = random.choice(list_value)

            column_dict[column["name"]] = value

        result.append(column_dict)
        column_dict = {}
        # time.sleep(5)
    return result


def upload_file(file_name):

    bucket = settings.AWS_STORAGE_BUCKET_NAME
    object_name = "media/" + file_name

    AWS_ACCESS_KEY_ID = settings.AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY = settings.AWS_SECRET_ACCESS_KEY

    s3_client = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )
    try:
        response = s3_client.upload_file(file_name, bucket, object_name, ExtraArgs={'ACL': 'public-read'})
    except ClientError as e:
        logging.error(e)
        return False
    return True


def create_models(data, user):
    schema_name = data["name"]
    char = data["char"]
    sep = data["sep"]
    columns = data["columns"]
    filename = schema_name + ".csv"

    schema = Schema(
        name=schema_name, char=char, sep=sep, author_id=user.id, filename=filename
    )
    schema.save()

    for column in columns:
        coltype = column["type"]

        col = Column(
            name=column["name"],
            columntype=coltype,
            schema=schema,
            order=column["order"],
        )
        if coltype == "int":
            col.intfrom = column["from"]
            col.intto = column["to"]
        col.save()


def get_columns_data(schema_id):
    schema = Schema.objects.filter(pk=schema_id).first()
    columns = schema.columns.all()
    columns_data = []

    for column in columns:
        columns_data.append(
            {
                "name": column.name,
                "type": column.columntype,
                "order": column.order,
                "from": column.intfrom,
                "to": column.intto,
            }
        )
    return columns_data
