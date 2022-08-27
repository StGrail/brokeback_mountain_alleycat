from rest_framework import routers

from bot_settings.viewsets import RegistrationTextsViewSet
from geo_points.viewsets import GeoPointsViewSet, PointsExcludeViewSet
from participants.viewsets import ParticipantsViewSet
from race.viewsets import RaceViewSet, RaceDataViewSet

router = routers.DefaultRouter()

router.register(prefix=r'participants', viewset=ParticipantsViewSet, basename='participants')
router.register(prefix=r'bot_settings', viewset=RegistrationTextsViewSet, basename='bot-settings')
router.register(prefix=r'all_get_points', viewset=GeoPointsViewSet, basename='all-geo-points')
router.register(prefix=r'race', viewset=RaceViewSet, basename='race')
router.register(prefix='race_data', viewset=RaceDataViewSet, basename='race-data')
router.register(prefix='exclude', viewset=PointsExcludeViewSet, basename='exclude')
