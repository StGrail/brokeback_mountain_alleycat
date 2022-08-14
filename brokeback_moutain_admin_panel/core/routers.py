from rest_framework import routers

from bot_settings.viewsets import RegistrationTextsViewSet
from participants.viewsets import ParticipantsViewSet

router = routers.DefaultRouter()

router.register(
    prefix=r"participants", viewset=ParticipantsViewSet, basename="participants"
)
router.register(
    prefix=r"bot_settings", viewset=RegistrationTextsViewSet, basename='bot-settings'
)
