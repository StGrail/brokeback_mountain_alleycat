# Generated by Django 4.1 on 2022-08-10 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("race", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="race",
            name="time_of_race",
            field=models.DateTimeField(
                blank=True,
                default=None,
                null=True,
                verbose_name="Время, затраченное на гонку",
            ),
        ),
    ]
