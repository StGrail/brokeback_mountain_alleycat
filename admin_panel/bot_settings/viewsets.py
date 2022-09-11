from rest_framework import viewsets

from bot_settings.models import RegistrationTexts
from bot_settings.serializers import RegistrationTextsSerializer


class RegistrationTextsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RegistrationTexts.objects.only()
    serializer_class = RegistrationTextsSerializer
