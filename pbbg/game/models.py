from django.db import models

class ResourceTypes(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Actions(models.Model):
    action_type = models.CharField(max_length=20)
    def __str__(self):
        return self.action_type

# Add action items: search (for wood, at first), explore - has a chance to generate enemy.
# Add view with a post to Actions, with the payload being what action they want to do.
# Would need extending later with multiple views, but this will work for now.

class RpgStats(models.Model):
    strength = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    wisdom = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    charisma = models.IntegerField(default=1)

class Equipment(models.Model):
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

class Entities(models.Model):
    name = models.CharField(max_length=100)
    health = models.IntegerField(default=0)
    stats = models.ForeignKey(RpgStats, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, default=None, blank=True, null=True)

class Player(models.Model):
    owner = models.ForeignKey('auth.User', related_name='players', on_delete=models.CASCADE)
    identity = models.ForeignKey(Entities, on_delete=models.CASCADE)
    hunger = models.IntegerField(default=0)
    def __str__(self):
        return f'Name: {self.identity.name} - Health: {self.identity.health} - Hunger: {self.hunger}'
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