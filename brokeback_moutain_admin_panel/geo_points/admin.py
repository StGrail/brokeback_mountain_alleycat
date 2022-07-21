from django.contrib import admin

from geo_points.models import GeoPoints


@admin.register(GeoPoints)
class GeoPointsAdmin(admin.ModelAdmin):
    pass
