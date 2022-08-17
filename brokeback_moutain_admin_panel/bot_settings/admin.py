from django.contrib import admin
from solo.admin import SingletonModelAdmin

from bot_settings.models import RegistrationTexts, CustomMessage


@admin.register(RegistrationTexts)
class RegistrationTextsAdmin(SingletonModelAdmin):
    pass


@admin.register(CustomMessage)
class CustomMessageAdmin(SingletonModelAdmin):
    pass
