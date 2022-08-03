from django.contrib import admin

from race.models import Race, RaceAlbum, RacePhoto


@admin.register(RacePhoto)
class RacePhotoInlineAdmin(admin.ModelAdmin):
    pass


@admin.register(RaceAlbum)
class RaceAlbumInlineAdmin(admin.ModelAdmin):
    inlines = [
        RacePhotoInlineAdmin,
    ]


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    inlines = [RaceAlbumInlineAdmin]
