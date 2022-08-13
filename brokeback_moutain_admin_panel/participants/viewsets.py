from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from participants.models import Participant
from participants.serializers import ParticipantSerializer, ParticipantUpdateSerializer


class ParticipantsViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    lookup_field = "tg_chat_id"

    def get_serializer_class(self):
        """Убираем поле tg_chat_id из сериалайзера при апдейте"""

        if self.action in ("partial_update", "update"):
            return ParticipantUpdateSerializer
        return ParticipantSerializer

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
