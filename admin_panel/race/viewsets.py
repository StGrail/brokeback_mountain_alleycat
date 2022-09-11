from rest_framework import viewsets, status
from rest_framework.response import Response

from race.models import Race, RaceData
from race.serializers import RaceUpdateSerializer, RaceSerializer, RaceDataSerializer


class RaceViewSet(viewsets.ModelViewSet):
    """Обновление инстанса гонки"""

    queryset = Race.objects.all()
    lookup_field = 'participant__tg_chat_id'

    def get_serializer_class(self):
        """Убираем поле tg_chat_id из сериалайзера при апдейте"""

        if self.action in ("partial_update", "update"):
            return RaceUpdateSerializer
        return RaceSerializer

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class RaceDataViewSet(viewsets.ReadOnlyModelViewSet):
    """Получение всех данных по гонке"""

    queryset = RaceData.objects.all()
    serializer_class = RaceDataSerializer
