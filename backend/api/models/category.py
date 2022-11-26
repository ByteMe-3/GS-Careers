from django.contrib import admin
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name_plural = "Categories"


admin.site.register(Category)
