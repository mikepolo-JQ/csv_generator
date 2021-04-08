import csv
import json
import random
import time

import boto3

from applications.generator.models import Column
from applications.generator.models import Schema
from django.conf import settings
import logging
import boto3
from botocore.exceptions import ClientError


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


def get_columns_values(columns) -> list:
    result = []
    column_dict = {}
    rows_count = 3

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


def generate_csv(data):
    schema_name = data["name"]
    filename = schema_name + ".csv"
    char = data["char"]
    sep = data["sep"]
    columns = data["columns"]
    columns.sort(key=lambda i: i["order"])

    rows = get_columns_values(columns)

    BUCKET_NAME = settings.AWS_STORAGE_BUCKET_NAME
    OBJECT_NAME = 'media/' + filename
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
    res = upload_file(file_name=filename, bucket=BUCKET_NAME, object_name=OBJECT_NAME)
    if res:
        print("Ready")


def upload_file(file_name, bucket, object_name=None):

    if object_name is None:
        object_name = file_name

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def create_models(data, user):
    schema_name = data["name"]
    char = data["char"]
    sep = data["sep"]
    columns = data["columns"]

    schema = Schema(name=schema_name, char=char, sep=sep, author_id=user.id)
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
