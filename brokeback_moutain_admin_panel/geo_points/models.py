from django.db import models


class GeoPoints(models.Model):
    """Модель участника гонки"""

    name = models.CharField(verbose_name='Название точки', max_length=64)
    longitude_start = models.DecimalField(
        verbose_name='Долгота старта участка', max_digits=9, decimal_places=6
    )
    latitude_start = models.DecimalField(
        verbose_name='Широта старта участка', max_digits=9, decimal_places=6
    )
    longitude_finish = models.DecimalField(
        verbose_name='Долгота финиша участка', max_digits=9, decimal_places=6
    )
    latitude_finish = models.DecimalField(
        verbose_name='Широта финиша участка', max_digits=9, decimal_places=6
    )

    class Meta:
        verbose_name = 'Точка'
        verbose_name_plural = 'Точки'

    def __str__(self):
        return self.name
