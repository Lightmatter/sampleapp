# Generated by Django 3.0.7 on 2020-06-24 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="test_field",
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
