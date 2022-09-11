from django.db import models
from solo.models import SingletonModel


class RegistrationTexts(SingletonModel):
    welcome_message = models.TextField(
        'Welcome message', help_text='Отправляем при первом входе в бота'
    )
    race_disclaimer = models.TextField(
        'Дисклеймер перед регистрацией',
        help_text='Можно указать примерную инфу о механике гонки/соглашение, что никто не несет ответсвенность',
    )
    after_reg_message = models.TextField(
        'Сообщение после регистрации', help_text='Можно указать информацию о месте и времени сбора'
    )

    class Meta:
        verbose_name = "Текст для регистрации в боте"
        verbose_name_plural = "Тексты для регистрации в боте"

    def __str__(self):
        return 'Текст для регистрации'


class CustomMessage(SingletonModel):
    start_message = models.TextField('Сообщение о старте', help_text='Отправляем для старта гонки')
    winner_message = models.TextField(
        'Сообщение для победителей', help_text='Отправляем выбранным участникам'
    )
    custom_message = models.TextField(
        'Кастомное сообщение для всех', blank=True, help_text='Отправляем всем участникам'
    )

    class Meta:
        verbose_name = "Текст для гонки"
        verbose_name_plural = "Тексты для гонки"

    def __str__(self):
        return 'Текст для гонки'
