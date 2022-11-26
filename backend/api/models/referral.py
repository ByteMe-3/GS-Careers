from django.contrib import admin
from django.db import models
from .user import UserProfile
import datetime


class Referral(models.Model):
    link = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL)
    expire_date = models.DateTimeField(default=(datetime.datetime.now() + datetime.timedelta(days=1)))

    def __str__(self) -> str:
        return str(self.link)


admin.site.register(Referral)
