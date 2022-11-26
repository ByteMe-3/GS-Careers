from django.contrib import admin
from django.db import models
from .category import Category
from .task import Task


class Contest(models.Model):
    categories = models.ManyToManyField(Category)
    tasks = models.ManyToManyField(Task)
    open_time = models.DateTimeField(null=True, blank=True)
    close_time = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.user)


admin.site.register(Contest)
