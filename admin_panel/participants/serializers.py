from rest_framework import serializers

from participants.constants import CATEGORY_CHOICES
from participants.models import Participant


class ParticipantSerializer(serializers.ModelSerializer):
    category_readable_name = serializers.SerializerMethodField(required=False, read_only=True)

    class Meta:
        model = Participant
        fields = ["name", "category", "category_readable_name", "instagram", "tg_chat_id", "registration_date"]
        read_only_fields = ["registration_date"]

    @staticmethod
    def get_category_readable_name(obj):
        return str(CATEGORY_CHOICES[obj.category][1])


class ParticipantUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = [
            "name",
            "category",
            "instagram",
        ]
