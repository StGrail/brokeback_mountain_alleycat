from ckeditor.fields import RichTextField
from solo.models import SingletonModel


class RegistrationTexts(SingletonModel):
    welcome_message = RichTextField(
        'Welcome message', help_text='Отправляем при первом входе в бота'
    )
    race_disclaimer = RichTextField(
        'Дисклеймер перед регистрацией',
        help_text='Можно указать примерную инфу о механике гонки/соглашение, что никто не несет ответсвенность',
    )
    after_reg_message = RichTextField(
        'Сообщение после регистрации', help_text='Можно указать информацию о месте и времени сбора'
    )

    class Meta:
        verbose_name = "Текст для регистрации в боте"
        verbose_name_plural = "Тексты для регистрации в боте"

    def __str__(self):
        return 'Текст для регистрации'
