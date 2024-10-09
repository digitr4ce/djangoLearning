from rest_framework import generics

from .models import Player
from .serializers import PlayerSerializer

class PlayerList(generics.ListCreateAPIView):
    """
    List all players, or create a new player.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a player instance.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer