from django.db import models

from participants.constants import CATEGORY_CHOICES


class Participant(models.Model):
    """Модель участника гонки"""

    name = models.CharField(verbose_name='Имя', max_length=64)
    category = models.IntegerField(
        verbose_name='Категория', choices=CATEGORY_CHOICES, default=0
    )
    instagram = models.CharField(
        verbose_name='Инстаграм',
        max_length=64,
        help_text='запрещенная организация на территории Российской Федерации',
        blank=True,
    )
    registration_date = models.DateTimeField(verbose_name='Время регистрации', auto_now_add=True)

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    def __str__(self):
        return self.name
