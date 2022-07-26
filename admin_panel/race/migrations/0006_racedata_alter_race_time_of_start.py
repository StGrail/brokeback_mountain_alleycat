# Generated by Django 4.1 on 2022-08-21 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("race", "0005_alter_race_participant_alter_race_points"),
    ]

    operations = [
        migrations.CreateModel(
            name="RaceData",
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
                    "time_of_start",
                    models.DateTimeField(
                        blank=True,
                        help_text="Автоматически сохраняется при отправке сообщения о начале гонки",
                        null=True,
                        verbose_name="Время старта гонки",
                    ),
                ),
                (
                    "is_started",
                    models.BooleanField(
                        default=False, verbose_name="Закрыта ли регистрация"
                    ),
                ),
            ],
            options={
                "verbose_name": "Время старта гонки",
                "verbose_name_plural": "Время старта гонки",
            },
        ),
        migrations.AlterField(
            model_name="race",
            name="time_of_start",
            field=models.DateTimeField(blank=True, verbose_name="Время старта"),
        ),
    ]
