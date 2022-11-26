from django.contrib import admin
from django.db import models


class Config(models.Model):
    name = models.CharField(max_length=100, null=True, unique=True)
    text_value = models.CharField(max_length=100, null=True, blank=True)
    int_value = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name)


admin.site.register(Config)
