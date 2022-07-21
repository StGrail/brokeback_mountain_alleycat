from django.db import models


class GeoPoints(models.Model):
    """Модель участника гонки"""

    name = models.CharField(verbose_name='Название точки', max_length=64)
    longitude = models.DecimalField(verbose_name='Долгота', max_digits=9, decimal_places=6)
    latitude = models.DecimalField(verbose_name='Широта', max_digits=9, decimal_places=6)

    class Meta:
        verbose_name = 'Точка'
        verbose_name_plural = 'Точки'

    def __str__(self):
        return self.name
