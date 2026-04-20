from rest_framework.viewsets import ModelViewSet
from library.models import Event
from library.serializers import EventSerializer

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


