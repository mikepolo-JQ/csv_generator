import json
import random
import time


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
    "name": ["Johnny Depp", "Al Pacino", "Robert De Niro", "Kevin Spacey", "Denzel Washington"],
    "company": ["Google", "Coca-cola", "Nike", "Adidas", "Ebay"],
    "date": ["2020.01.03", "2015.06.14", "2010.04.23", "2017.05.07", "2021.04.08"]
}


def get_columns_values(columns) -> list:
    result = []
    column_dict = {}
    rows_count = 3

    for i in range(rows_count):
        for column in columns:
            list_value = column_values[column['type']]

            if not list_value:
                value = random.randint(int(column['from']), int(column['to']))
            else:
                value = random.choice(list_value)

            column_dict[column['name']] = value

        result.append(column_dict)
        column_dict = {}
        # time.sleep(5)
    return result
