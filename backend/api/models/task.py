from django.contrib import admin
from django.db import models

from .category import Category


class Task(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    reward = models.IntegerField(default=0)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL
    )
    TYPES = [
        ("question", "question"),
        ("code", "code"),
        ("action", "action"),
        ("quiz", "quiz"),
    ]
    type = models.CharField(
        max_length=32,
        choices=TYPES,
        default="question",
    )

    def __str__(self) -> str:
        return str(self.id)


admin.site.register(Task)
