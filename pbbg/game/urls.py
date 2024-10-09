from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include

from . import views

from snippets.views import api_root, PlayerViewSet, UserViewSet

player_list = PlayerViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
player_detail = PlayerViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

app_name = "game"
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path("player/", player_list, name="player-list"),
    path("player/<int:pk>/", player_detail, name="player-detail"),
    path('user/', user_list, name="user-list"),
    path('user/<int:pk>/', user_detail, name="user-detail"),
])

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]