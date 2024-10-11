from rest_framework import serializers
from game.models import Player, InventoryItems, Inventory
from django.contrib.auth.models import User

class InventoryItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItems
        fields = ['id', 'resource_type', 'quantity']

class InventorySerializer(serializers.ModelSerializer):
    inventory_items = InventoryItemsSerializer(many=True)

    class Meta:
        model = Inventory
        fields = ['id', 'inventory_items']


class PlayerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    inventory = InventoryItemsSerializer()

    class Meta:
        model = Player
        fields = ['id', 'hunger', 'owner', 'inventory']

class UserSerializer(serializers.ModelSerializer):
    players = serializers.PrimaryKeyRelatedField(many=True, queryset=Player.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'players']
