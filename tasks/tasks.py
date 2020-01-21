from celery import shared_task
from django.db import transaction

from .models import Issue


@shared_task
def create_new_issue(name: str) -> None:
    with transaction.atomic():
        Issue.objects.create_issue(name=name)
