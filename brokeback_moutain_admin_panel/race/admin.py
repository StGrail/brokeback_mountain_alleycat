from django.contrib import admin

from race.models import Race, RaceAlbum, RacePhoto


# @admin.register(RacePhoto)
# class RacePhotoInlineAdmin(admin.TabularInline):
#     pass
#
#
# @admin.register(RaceAlbum)
# class RaceAlbumInlineAdmin(admin.TabularInline):
#     inlines = [
#         RacePhotoInlineAdmin,
#     ]


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    # inlines = [RaceAlbumInlineAdmin]
    pass