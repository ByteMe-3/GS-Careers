# Generated by Django 4.1.3 on 2022-11-26 06:06

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0014_alter_referral_expire_date_alter_task_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="referral",
            name="expire_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 11, 27, 7, 6, 37, 626864)
            ),
        ),
    ]
