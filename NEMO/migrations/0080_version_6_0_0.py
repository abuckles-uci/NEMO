# Generated by Django 3.2.25 on 2024-04-17 16:18

from django.db import migrations

from NEMO.migrations_utils import create_news_for_version


class Migration(migrations.Migration):

    dependencies = [
        ("NEMO", "0079_user_active_access_expiration_verbose_names"),
    ]

    def new_version_news(apps, schema_editor):
        create_news_for_version(apps, "6.0.0", "")

    operations = [
        migrations.RunPython(new_version_news),
    ]
