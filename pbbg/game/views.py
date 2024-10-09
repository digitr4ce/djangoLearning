from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions

from django.contrib.auth.models import User

from .models import Player
from .serializers import PlayerSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

class PlayerList(generics.ListCreateAPIView):
    """
    List all players, or create a new player.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a player instance.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('game:user-list', request=request, format=format),
        'players': reverse('game:player-list', request=request, format=format)
    })