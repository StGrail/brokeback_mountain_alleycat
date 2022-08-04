from django.db import models

from participants.models import Participant


class Race(models.Model):
    """Модель гонки"""

    participant = models.ForeignKey(
        Participant, verbose_name='Участник', on_delete=models.CASCADE
    )
    time_of_start = models.DateTimeField('Время старта', blank=True)
    time_of_finish = models.DateTimeField('Время финиша', blank=True)
    place = models.SmallIntegerField('Место в общем зачёте', default=0)
    place_in_category = models.PositiveSmallIntegerField('Место в категории', default=0)
    points = models.ManyToManyField(
        'geo_points.GeoPoints', verbose_name='Точки, которые были финишированы'
    )
    photos = models.ForeignKey(
        'race.RaceAlbum', verbose_name='Фотографии с гонки', on_delete=models.CASCADE
    )
    is_finished = models.BooleanField('Закончил гонку', default=False)

    class Meta:
        verbose_name = 'Гонка'
        verbose_name_plural = 'Гонка'

    def __str__(self):
        return f'{str(self.participant.name)} - место общ: {self.place}'


class RaceAlbum(models.Model):
    race_result = models.ForeignKey(Race, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Альбом с фотографиями'
        verbose_name_plural = 'Альбомы с фотографиями'

    def __str__(self):
        return str(self.race_result.participant.name)


class RacePhoto(models.Model):
    album = models.ForeignKey(RaceAlbum, verbose_name='Альбом', on_delete=models.CASCADE)
    photo = models.ImageField('Фотография', upload_to='photos', blank=True)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотография'

    def __str__(self):
        return str(self.album.race_result.participant.name)


