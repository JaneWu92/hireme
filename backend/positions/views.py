from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Position
from .serializers import PositionSerializer

class PositionListView(ListAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer