from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include


from . import views

app_name = "game"
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path("player/", views.PlayerList.as_view(), name="player-list"),
    path("player/<int:pk>/", views.PlayerDetail.as_view(), name="player-detail"),
    path('user/', views.UserList.as_view(), name="user-list"),
    path('user/<int:pk>/', views.UserDetail.as_view(), name="user-detail"),
])

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]