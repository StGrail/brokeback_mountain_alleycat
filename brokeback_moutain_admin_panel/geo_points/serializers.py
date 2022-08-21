from rest_framework import serializers

from geo_points.models import GeoPoints


class GeoPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoPoints
        fields = '__all__'
