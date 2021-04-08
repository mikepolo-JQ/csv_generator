from celery import shared_task

from applications.generator.utils import generate_csv


@shared_task
def celery_generator_csv(data):
    generate_csv(data)
