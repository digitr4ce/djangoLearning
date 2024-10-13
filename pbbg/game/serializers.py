from rest_framework import serializers
from game.models import Player, InventoryItems, Inventory, ResourceTypes, RpgStats, Entities, Equipment, House, Actions
from django.contrib.auth.models import User

class ResourceTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceTypes
        fields = ['id', 'name']

class RpgStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RpgStats
        fields = ['id', 'strength', 'intelligence', 'wisdom', 'dexterity', 'charisma']

class EquimentSerializer(serializers.ModelSerializer):
    stat_upgrades = RpgStatsSerializer()

    class Meta:
        model = Equipment
        fields = ['id', 'stat_upgrades', 'equipment_type', 'equipment_material']

class EntitiesSerializer(serializers.ModelSerializer):
    stats = RpgStatsSerializer()
    equipment = EquimentSerializer(read_only=True)
    
    class Meta:
        model = Entities
        fields = ['id', 'name', 'health', 'stats', 'equipment']

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
    inventory = InventoryItemsSerializer(read_only=True)
    identity = EntitiesSerializer()

    class Meta:
        model = Player
        fields = ['id', 'hunger', 'owner', 'identity', 'inventory']

    def create(self, validated_data):
        rpg_stats = RpgStats.objects.create(**validated_data['identity']['stats'])
        identity = Entities.objects.create(
            name = validated_data['identity']['name'],
            health = validated_data['identity']['health'],
            stats = rpg_stats,
        )
        player = Player.objects.create(
            owner = validated_data['owner'],
            hunger = validated_data['hunger'],
            identity = identity,
        )
        return player

    
class UserSerializer(serializers.ModelSerializer):
    players = serializers.PrimaryKeyRelatedField(many=True, queryset=Player.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'players']

class HouseSerializer(serializers.ModelSerializer):
    owner = PlayerSerializer(read_only = True)

    class Meta:
        model = House
        fields = ['id', 'owner']

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actions
        fields = ['id', 'action_type']