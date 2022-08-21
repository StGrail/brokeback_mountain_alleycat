from django.db import models
from solo.models import SingletonModel

from participants.models import Participant


class Race(models.Model):
    """Модель гонки"""

    participant = models.OneToOneField(
        Participant, verbose_name="Участник", to_field='tg_chat_id', on_delete=models.CASCADE
    )
    time_of_start = models.DateTimeField("Время старта", blank=True)
    time_of_finish = models.DateTimeField("Время финиша", blank=True, null=True)
    time_of_race = models.DateTimeField(
        "Время, затраченное на гонку", default=None, null=True, blank=True
    )
    place = models.SmallIntegerField("Место в общем зачёте", default=0)
    place_in_category = models.PositiveSmallIntegerField("Место в категории", default=0)
    points = models.ManyToManyField(
        "geo_points.GeoPoints",
        verbose_name="Точки, которые были финишированы",
        blank=True,
    )
    # photos = models.ForeignKey(
    #     "race.RaceAlbum", verbose_name="Фотографии с гонки", on_delete=models.CASCADE
    # )
    is_finished = models.BooleanField("Закончил гонку", default=False)

    class Meta:
        verbose_name = "Гонка"
        verbose_name_plural = "Гонка"

    def __str__(self):
        return f"{str(self.participant.name)} - место общ: {self.place}"


# class RaceAlbum(models.Model):
#     race_result = models.ForeignKey(Race, on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name = "Альбом с фотографиями"
#         verbose_name_plural = "Альбомы с фотографиями"
#
#     def __str__(self):
#         return str(self.race_result.participant.name)
#
#
# class RacePhoto(models.Model):
#     album = models.ForeignKey(
#         RaceAlbum, verbose_name="Альбом", on_delete=models.CASCADE
#     )
#     photo = models.ImageField("Фотография", upload_to="photos", blank=True)
#
#     class Meta:
#         verbose_name = "Фотография"
#         verbose_name_plural = "Фотография"
#
#     def __str__(self):
#         return str(self.album.race_result.participant.name)


class RaceData(SingletonModel):
    time_of_start = models.DateTimeField(
        'Время старта гонки',
        help_text='Автоматически сохраняется при отправке сообщения о начале гонки',
        blank=True,
        null=True,
    )
    is_started = models.BooleanField('Закрыта ли регистрация', default=False)

    class Meta:
        verbose_name = "Время старта гонки"
        verbose_name_plural = "Время старта гонки"
