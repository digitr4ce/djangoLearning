from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import status

from rest_framework.views import APIView

from django.contrib.auth.models import User

from .models import Player, Actions, Entities
from .serializers import PlayerSerializer, UserSerializer, ActionSerializer
from .permissions import IsOwnerOrReadOnly


class PlayerViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActionsView(APIView):
    """
    List possible actions or simulate exploration or a fight.
    """

    def get(self, request, format=None):
        actions = Actions.objects.all()
        serializer = ActionSerializer(actions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # We assume only one character can be named in a certain way.
        # TODO: implement the above restriction.
        try:
            player_identity = Entities.objects.filter(name=request.data["player_name"])
            is_owner = Player.objects.filter(
                owner=request.user, identity_id=player_identity[0].id
            )
            action = request.data["action"]
        except (AttributeError, KeyError) as e:
            return Response(
                data="You must specifiy both an action and a player name.",
                status=status.HTTP_400_BAD_REQUEST,
            )
        except UnboundLocalError as e:
            return Response(
                data="You must specify an action and a player name that exist.",
                status=status.HTTP_400_BAD_REQUEST,
            )
        action_query = Actions.objects.filter(action_type=action)
        if action_query.count() == 0:
            return Response(data="Unknown action.", status=status.HTTP_400_BAD_REQUEST)
        if is_owner.count() == 0:
            return Response(
                data="You do not have permission to use this character.",
                status=status.HTTP_400_BAD_REQUEST,
            )
        # TODO: Check for resource type in the POST, if search is added, same as with action.
        # TODO: Create code that updates database values and adds experience points and resources to character if they defeat the enemy.
