import json
from datetime import datetime

from django.contrib import admin, messages
from django.shortcuts import redirect
from django.urls import reverse

from bot_settings.keyboards import KEYBOARDS
from bot_settings.models import CustomMessage
from bot_settings.services import TelegramApiRequest
from participants.models import Participant
from race.models import RaceData


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    fields = (
        "name",
        "category",
        "instagram",
        "tg_chat_id",
    )
    list_display = (
        "tg_chat_id",
        "name",
        "category",
        "registration_date",
    )
    list_filter = ("category",)
    ordering = ("-registration_date",)
    readonly_fields = ("tg_chat_id",)
    actions = [
        'send_start_message_to_participants',
        'send_custom_message_to_participants',
    ]

    @admin.action(description='Отправить сообщение о старте всем амигос')
    def send_start_message_to_participants(self, request, queryset):
        chat_ids = self.get_all_participants_tg_chat_ids()
        try:
            message = CustomMessage.objects.first().start_message
            keyboard = json.dumps(KEYBOARDS.get('ready_to_race'))
            TelegramApiRequest(
                chat_ids=chat_ids, message=message, keyboard=keyboard
            ).send_message_to_users_with_keyboard()
            race_data = RaceData.objects.first()
            race_data.time_of_start = datetime.now()
            race_data.is_started = True
            race_data.save()
            messages.add_message(request, messages.SUCCESS, f'Собщение отправлено всем участникам')
        except AttributeError:
            messages.add_message(request, messages.ERROR, f'Заполните поле в админке')
            url = reverse('admin:bot_settings_custommessage_change')
            return redirect(url)

    @admin.action(description='Отправить кастомное сообщение всем амигос')
    def send_custom_message_to_participants(self, request, queryset):
        chat_ids = self.get_all_participants_tg_chat_ids()
        try:
            message = CustomMessage.objects.first().custom_message
            TelegramApiRequest(chat_ids=chat_ids, message=message).send_message_to_users()
            messages.add_message(request, messages.SUCCESS, f'Собщение отправлено всем участникам')
        except AttributeError:
            messages.add_message(request, messages.ERROR, f'Заполните поле в админке')
            url = reverse('admin:bot_settings_custommessage_change')
            return redirect(url)

    @staticmethod
    def get_all_participants_tg_chat_ids():
        chat_ids = Participant.objects.all().values_list('tg_chat_id', flat=True)
        return chat_ids
