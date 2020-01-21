from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Tasks


@receiver(pre_save, Tasks)
def task_save_handler(sender, **kwargs):
    print("sygnal")