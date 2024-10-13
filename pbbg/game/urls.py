from rest_framework.routers import DefaultRouter
from django.urls import path, include

from . import views

router = DefaultRouter()
router.register("players", views.PlayerViewSet, basename="player")
router.register("users", views.UserViewSet, basename="user")


app_name = "game"
urlpatterns = [
    path("", include(router.urls)),
    path("actions/", views.ActionsView.as_view(), name="actions"),
]
