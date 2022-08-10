from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin

from race.models import Race, RaceAlbum, RacePhoto


class RacePhotoInlineAdmin(InlineModelAdmin):
    model = RacePhoto


class RaceAlbumInlineAdmin(InlineModelAdmin):
    model = RaceAlbum
    inlines = [
        RacePhotoInlineAdmin,
    ]


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    # inlines = [RaceAlbumInlineAdmin]  # TODO
    fields = (
        'participant',
        'place',
        'place_in_category',
        'time_of_start',
        'time_of_finish',
        'time_of_race',
        'points',
        'is_finished',
    )
    list_filter = (
        'participant',
        'place',
        'place_in_category',
        'is_finished',
        'time_of_race',
    )
    readonly_fields = (
        'place',
        'place_in_category',
        'participant',
        'time_of_start',
        'time_of_finish',
        'time_of_race',
        'is_finished',
    )
