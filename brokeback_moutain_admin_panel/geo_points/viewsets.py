from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from geo_points import contstans
from geo_points.models import GeoPoints
from geo_points.serializers import GeoPointsSerializer


class GeoPointsViewSet(viewsets.ReadOnlyModelViewSet):
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
            'id': data.get('id')
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

    @action(methods=['GET'], detail=False, description='Получение финишных координат')
    def exclude(self, request, *args, **kwargs):
        points_list = request.data.get('exclude')
        if points_list:
            qs = self.queryset.exclude(id__in=points_list,).exclude(
                is_start_or_finish_point__in=(contstans.IS_FINISH, contstans.IS_START),
            )
        else:
            qs = self.queryset
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        if self.action in ['list']:
            queryset = self.queryset.exclude(
                is_start_or_finish_point__in=(contstans.IS_FINISH, contstans.IS_START)
            )
            return queryset
        else:
            return self.queryset
