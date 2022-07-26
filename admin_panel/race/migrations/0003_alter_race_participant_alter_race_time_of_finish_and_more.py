# Generated by Django 4.1 on 2022-08-18 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("participants", "0005_alter_participant_name"),
        ("race", "0002_race_time_of_race"),
    ]

    operations = [
        migrations.AlterField(
            model_name="race",
            name="participant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="participants.participant",
                to_field="tg_chat_id",
                verbose_name="Участник",
            ),
        ),
        migrations.AlterField(
            model_name="race",
            name="time_of_finish",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Время финиша"
            ),
        ),
        migrations.AlterField(
            model_name="race",
            name="time_of_start",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Время старта"),
        ),
    ]
