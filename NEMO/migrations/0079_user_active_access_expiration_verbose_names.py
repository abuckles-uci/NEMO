# Generated by Django 3.2.25 on 2024-05-02 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("NEMO", "0078_version_5_6_0"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="access_expiration",
            field=models.DateField(
                blank=True,
                help_text="The user will lose all access rights after this date. Typically this is used to ensure that safety training has been completed by the user every year.",
                null=True,
                verbose_name="active access expiration",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Designates whether this user can log in. Unselect this instead of deleting accounts.",
                verbose_name="active account",
            ),
        ),
    ]
