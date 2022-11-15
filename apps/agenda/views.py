from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from apps.agenda.serializers import AgendaSerializer
from apps.agenda.models import Agenda


class AgendaViewSet(ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    filterset_fields = ['fecha', 'conductor']
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']
