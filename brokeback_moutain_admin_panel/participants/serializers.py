from rest_framework import serializers

from participants.models import Participant


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ["name", "category", "instagram", "tg_chat_id", "registration_date"]
        read_only_fields = ["registration_date"]


class ParticipantUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = [
            "name",
            "category",
            "instagram",
        ]
