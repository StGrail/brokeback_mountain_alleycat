from django.contrib import admin

from geo_points.models import GeoPoints


@admin.register(GeoPoints)
class GeoPointsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_start_or_finish_point",
    )
    list_filter = ("is_start_or_finish_point",)
