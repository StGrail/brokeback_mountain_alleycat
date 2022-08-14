from django.contrib import admin

from participants.models import Participant


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
