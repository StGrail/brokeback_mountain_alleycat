from rest_framework import serializers

from bot_settings.models import RegistrationTexts


class RegistrationTextsSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegistrationTexts
        exclude = ("id",)
