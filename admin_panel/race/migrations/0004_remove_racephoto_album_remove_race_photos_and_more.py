# Generated by Django 4.1 on 2022-08-18 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("race", "0003_alter_race_participant_alter_race_time_of_finish_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="racephoto",
            name="album",
        ),
        migrations.RemoveField(
            model_name="race",
            name="photos",
        ),
        migrations.DeleteModel(
            name="RaceAlbum",
        ),
        migrations.DeleteModel(
            name="RacePhoto",
        ),
    ]