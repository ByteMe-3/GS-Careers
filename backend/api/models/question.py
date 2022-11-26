from django.contrib import admin
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Question(models.Model):
    question = models.CharField(max_length=100, null=True, blank=True)
    answers = ArrayField(models.CharField(max_length=100), size=4, null=True)
    rewards = ArrayField(models.IntegerField(), size=4, null=True)

    def __str__(self) -> str:
        return str(self.question)


admin.site.register(Question)
