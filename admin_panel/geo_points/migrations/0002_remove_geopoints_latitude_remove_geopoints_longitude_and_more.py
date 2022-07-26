# Generated by Django 4.1 on 2022-08-04 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("geo_points", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="geopoints",
            name="latitude",
        ),
        migrations.RemoveField(
            model_name="geopoints",
            name="longitude",
        ),
        migrations.AddField(
            model_name="geopoints",
            name="latitude_finish",
            field=models.DecimalField(
                decimal_places=6,
                max_digits=9,
                null=True,
                verbose_name="Широта финиша участка",
            ),
        ),
        migrations.AddField(
            model_name="geopoints",
            name="latitude_start",
            field=models.DecimalField(
                decimal_places=6,
                max_digits=9,
                null=True,
                verbose_name="Широта старта участка",
            ),
        ),
        migrations.AddField(
            model_name="geopoints",
            name="longitude_finish",
            field=models.DecimalField(
                decimal_places=6,
                max_digits=9,
                null=True,
                verbose_name="Долгота финиша участка",
            ),
        ),
        migrations.AddField(
            model_name="geopoints",
            name="longitude_start",
            field=models.DecimalField(
                decimal_places=6,
                max_digits=9,
                null=True,
                verbose_name="Долгота старта участка",
            ),
        ),
    ]
