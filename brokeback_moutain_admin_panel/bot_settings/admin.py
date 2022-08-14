from django.contrib import admin
from solo.admin import SingletonModelAdmin

from bot_settings.models import RegistrationTexts


@admin.register(RegistrationTexts)
class RegistrationTextsAdmin(SingletonModelAdmin):
    pass
