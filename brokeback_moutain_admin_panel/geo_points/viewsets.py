from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from geo_points import contstans
from geo_points.models import GeoPoints
from geo_points.serializers import GeoPointsSerializer
from race.models import Race


class GeoPointsViewSet(viewsets.ReadOnlyModelViewSet):
    """Получение гео точек из бд"""

    queryset = GeoPoints.objects.all()
    serializer_class = GeoPointsSerializer

    @action(methods=['GET'], detail=False, description='Получение стартовых координат')
    def start(self, request, *args, **kwargs):
        data = (
            self.queryset.filter(is_start_or_finish_point=contstans.IS_START)
            .values('longitude_start', 'latitude_start', 'id')
            .first()
        )
        response = {
            'longitude_start': data.get('longitude_start'),
            'latitude_start': data.get('latitude_start'),
            'id': data.get('id'),
        }

        return Response(response, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False, description='Получение финишных координат')
    def finish(self, request, *args, **kwargs):
        data = (
            self.queryset.filter(is_start_or_finish_point=contstans.IS_FINISH)
            .values('longitude_start', 'latitude_start', 'id')
            .first()
        )
        response = {
            'longitude_start': data.get('longitude_start'),
            'latitude_start': data.get('latitude_start'),
            'id': data.get('id'),
        }

        return Response(response, status=status.HTTP_200_OK)

    def get_queryset(self):
        if self.action in ['list']:
            queryset = self.queryset.exclude(
                is_start_or_finish_point__in=(contstans.IS_FINISH, contstans.IS_START)
            )
            return queryset
        else:
            return self.queryset


class PointsExcludeViewSet(viewsets.ReadOnlyModelViewSet):
    """Получение координат промежуточных точек"""

    queryset = GeoPoints.objects.all()
    serializer_class = GeoPointsSerializer

    def list(self, request, *args, **kwargs):
        tg_chat_id = request.query_params.get('tg_chat_id', False)
        if tg_chat_id:
            points = Race.objects.filter(participant__tg_chat_id=tg_chat_id).values('points')
            data = GeoPoints.objects.exclude(id__in=points).exclude(
                is_start_or_finish_point__in=(contstans.IS_FINISH, contstans.IS_START)
            )
            serializer = self.get_serializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        response = Response(data=dict())
        response.data['results'] = super().list(request, args, kwargs).data
        return response
