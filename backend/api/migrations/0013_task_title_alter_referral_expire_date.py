# Generated by Django 4.1.3 on 2022-11-26 02:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0012_alter_referral_expire_date_alter_userprofile_ref"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="title",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="referral",
            name="expire_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 11, 27, 3, 11, 35, 366681)
            ),
        ),
    ]