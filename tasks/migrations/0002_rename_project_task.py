# Generated by Django 4.1.7 on 2023-03-07 19:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0001_initial"),
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Project",
            new_name="Task",
        ),
    ]