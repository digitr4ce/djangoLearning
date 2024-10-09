from rest_framework import serializers
from game.models import Player
from django.contrib.auth.models import User

class PlayerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Player
        fields = ['id', 'name', 'health', 'hunger', 'owner']

class UserSerializer(serializers.ModelSerializer):
    # TODO: Rename Payers to Characters
    players = serializers.PrimaryKeyRelatedField(many=True, queryset=Player.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'players']
