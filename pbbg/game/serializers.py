from rest_framework import serializers
from game.models import Player

class PlayerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    health = serializers.IntegerField()
    hunger = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Player` instance, given the validated data.
        """
        return Player.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Player` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.health = validated_data.get('health', instance.health)
        instance.hunger = validated_data.get('hunger', instance.hunger)
        instance.save()
        return instance