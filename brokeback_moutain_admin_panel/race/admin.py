from datetime import datetime

from django.contrib import admin, messages
from django.contrib.admin.options import InlineModelAdmin

# from race.models import Race, RaceAlbum, RacePhoto
from django.shortcuts import redirect
from django.urls import reverse

from bot_settings.models import CustomMessage
from bot_settings.services import TelegramApiRequest
from race.models import Race, RaceData


# class RacePhotoInlineAdmin(InlineModelAdmin):
#     model = RacePhoto
#
#
# class RaceAlbumInlineAdmin(InlineModelAdmin):
#     model = RaceAlbum
#     inlines = [
#         RacePhotoInlineAdmin,
#     ]


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    # inlines = [RaceAlbumInlineAdmin]  # TODO
    fields = (
        "participant",
        # "place",
        # "place_in_category",
        "time_of_start",
        "time_of_finish",
        "time_of_race",
        "points",
        "is_finished",
    )
    list_display = (
        "participant",
        "is_finished",
        "time_of_start",
        "time_of_finish",
        "time_of_race",
        # "place",
        # "place_in_category",
    )
    list_filter = (
        "participant",
        "participant__category",
        # "place",
        # "place_in_category",
        "is_finished",
        "time_of_race",
    )
    readonly_fields = (
        # "place",
        # "place_in_category",
        "participant",
        "time_of_start",
        "time_of_finish",
        "time_of_race",
        "is_finished",
    )
    actions = [
        'send_winner_message_to_participants',
    ]
    ordering = ("-time_of_race",)

    @admin.action(description='Отправить сообщение о победе выбранным амигос')
    def send_winner_message_to_participants(self, request, queryset):
        chat_ids = queryset.values_list('participant__tg_chat_id', flat=True)
        try:
            message = CustomMessage.objects.first().winner_message
            TelegramApiRequest(chat_ids=chat_ids, message=message).send_message_to_users()
            messages.add_message(request, messages.SUCCESS, f'Собщение отправлено')
        except AttributeError:
            messages.add_message(request, messages.ERROR, f'Заполните поле в админке')
            url = reverse('admin:bot_settings_custommessage_change')
            return redirect(url)


@admin.register(RaceData)
class RaceDataAdmin(admin.ModelAdmin):
    pass
