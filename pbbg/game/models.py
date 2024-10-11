from django.db import models

class ResourceTypes(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class RpgStats(models.Model):
    strength = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    wisdom = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    charisma = models.IntegerField(default=1)

class Entities(models.Model):
    name = models.CharField(max_length=100)
    health = models.IntegerField(default=0)
    stats = models.ForeignKey(RpgStats, on_delete=models.CASCADE)

class Equipment(models.Model):
    owner = models.ForeignKey(Entities, on_delete=models.CASCADE)
    stat_upgrades = models.ForeignKey(RpgStats, on_delete=models.CASCADE)

    class EquipmentTypes(models.TextChoices):
        HEAD = 'head'
        L_HAND = 'l_hand',
        R_HAND = 'r_hand',
        TORSO = 'torso',
        LEGS = 'legs',
        FEET = 'feet',

    equipment_type = models.CharField(
        max_length = 10,
        choices=EquipmentTypes.choices,
        default=None,
    )

    class EquipmentMaterials(models.TextChoices):
        LIGHT = 'light',
        MEDIUM = 'medium',
        HEAVY = 'heavy',

    equipment_material = models.CharField(
        max_length = 10,
        choices = EquipmentMaterials.choices,
        default = None,
    )

class Player(models.Model):
    owner = models.ForeignKey('auth.User', related_name='players', on_delete=models.CASCADE)
    identity = models.ForeignKey(Entities, on_delete=models.CASCADE)
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

class House(models.Model):
    owner = models.ForeignKey(Player, on_delete=models.CASCADE)