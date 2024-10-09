from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


from . import views

app_name = "game"
urlpatterns = [
    path("", views.PlayerList.as_view(), name="index"),
    path("player/<int:player_id>/", views.PlayerDetail.as_view(), name="player"),
]

urlpatterns = format_suffix_patterns(urlpatterns)