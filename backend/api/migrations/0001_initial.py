# Generated by Django 4.1.3 on 2022-11-25 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reward", models.IntegerField(default=0)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("question", "question"),
                            ("code", "question"),
                            ("action", "question"),
                        ],
                        default="question",
                        max_length=32,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="profile"),
                ),
                ("points", models.IntegerField(default=0)),
                ("birth", models.DateField(blank=True, null=True)),
                ("categories", models.ManyToManyField(to="api.category")),
                ("done_tasks", models.ManyToManyField(to="api.task")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Contest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("open_time", models.DateTimeField(blank=True, null=True)),
                ("close_time", models.DateTimeField(blank=True, null=True)),
                ("categories", models.ManyToManyField(to="api.category")),
                ("tasks", models.ManyToManyField(to="api.task")),
            ],
        ),
    ]