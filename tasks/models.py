import datetime

from django.db import models

from model_utils.models import TimeStampedModel


class IssueManager(models.Manager):
    def create_issue(self, name):
        issue = self.create(name=name)
        issue.save()
        return issue


class Issue(TimeStampedModel):
    STATUS_NEW = 0
    STATUS_DONE = 9
    STATUS_CHOICES = (
        (STATUS_NEW, "Новая"),
        (STATUS_DONE, "Завершена")
    )

    status = models.SmallIntegerField(
        default=STATUS_NEW,
        choices=STATUS_CHOICES
    )

    name = models.CharField(
        verbose_name="Название задачи",
        max_length=128,
    )

    complete_time = models.DateTimeField(null=True, blank=True)

    objects = IssueManager()

    def save(self, *args, **kwargs):
        if self.pk is not None:
            origin = Issue.objects.get(pk=self.pk)
            if self.status != origin.status and self.status == self.STATUS_DONE:
                self.complete_time = datetime.datetime.now()
        super(Issue, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        
