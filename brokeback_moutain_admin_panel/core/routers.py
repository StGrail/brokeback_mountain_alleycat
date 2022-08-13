from rest_framework import routers

from participants.viewsets import ParticipantsViewSet

router = routers.DefaultRouter()

router.register(
    prefix=r"participants", viewset=ParticipantsViewSet, basename="participants"
)
