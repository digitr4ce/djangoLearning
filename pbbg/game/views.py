from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views import generic

from .models import Player

class IndexView(generic.ListView):
    template_name = "game/index.html"
    
    def get_queryset(self):
        """Return the list of players."""
        return Player.objects.order_by("name")
    

def player(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    return render(request, "game/player.html", {"player": player})
