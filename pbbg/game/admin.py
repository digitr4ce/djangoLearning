from django.contrib import admin

from .models import Player, ResourceTypes, Inventory, InventoryItems

admin.site.register([Player, ResourceTypes, Inventory, InventoryItems])
