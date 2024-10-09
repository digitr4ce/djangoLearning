from django.db import models

class ResourceTypes(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Player(models.Model):
    owner = models.ForeignKey('auth.User', related_name='players', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    health = models.IntegerField(default=0)
    hunger = models.IntegerField(default=0)
    def __str__(self):
        return f'Name: {self.name} - Health: {self.health} - Hunger: {self.hunger}'
    def is_hungry(self):
        return self.hunger >= 60

class Inventory(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    def __str__(self):
        return f'Inventory for player {self.player.name}'

class InventoryItems(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    resource_type = models.ForeignKey(ResourceTypes, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.resource_type.name}, quantity {self.quantity}, in {self.inventory}'



