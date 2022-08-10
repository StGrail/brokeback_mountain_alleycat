from django.db import models

from geo_points.contstans import START_OR_FINISH


class GeoPoints(models.Model):
    """Модель участника гонки"""

    name = models.CharField(verbose_name='Название точки', max_length=64)
    longitude_start = models.DecimalField(
        verbose_name='Долгота старта участка',
        max_digits=9,
        decimal_places=6,
        null=True,
    )
    latitude_start = models.DecimalField(
        verbose_name='Широта старта участка',
        max_digits=9,
        decimal_places=6,
        null=True,
    )
    longitude_finish = models.DecimalField(
        verbose_name='Долгота финиша участка',
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )
    latitude_finish = models.DecimalField(
        verbose_name='Широта финиша участка',
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )
    is_start_or_finish_point = models.SmallIntegerField(
        'Является стартовой или финишной точкой',
        choices=START_OR_FINISH,
        help_text='Устанавливаем только широту/долготу старта участка',
        null=True,
        default=0,
    )

    class Meta:
        verbose_name = 'Точка'
        verbose_name_plural = 'Точки'

    def __str__(self):
        return self.name
