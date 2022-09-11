from rest_framework import serializers

from race.models import Race, RaceData


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = [
            'participant',
            'time_of_start',
            'points',
            # 'photos',
            'is_finished',
        ]


class RaceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = [
            'participant',
            'time_of_start',
            'time_of_finish',
            'points',
            # 'photos',
            'is_finished',
        ]


class RaceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaceData
        fields = '__all__'
