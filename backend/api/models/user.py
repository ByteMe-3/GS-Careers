from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

from .category import Category
from .task import Task


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    image = models.ImageField(blank=True, null=True, upload_to="profile")
    points = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category, blank=True)
    done_tasks = models.ManyToManyField(Task, blank=True)
    birth = models.DateField(blank=True, null=True)
    ref = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return str(self.user)


admin.site.register(UserProfile)
