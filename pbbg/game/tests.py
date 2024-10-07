from django.test import TestCase
from django.urls import reverse

from .models import Player

class PlayerModelTests(TestCase):
    def test_is_hungry_with_lower_value(self):
        """
        is_hungry() returns False for players whose hunger is below 60.
        """
        player = Player(name='John', health=100, hunger=10)
        self.assertIs(player.is_hungry(), False)
    def test_is_hungry_with_higher_value(self):
        """
        is_hungry() returns True for players whose hunger is above 60.
        """
        player = Player(name='John', health=100, hunger=95)
        self.assertIs(player.is_hungry(), True)
    def test_is_hungry_with_equal_value(self):
        """
        is_hungry() return True for players whose hunger is 60.
        """
        player = Player(name='John', health=100, hunger=60)
        self.assertIs(player.is_hungry(), True)

class GameIndexViewTests(TestCase):
    def test_no_players(self):
        """
        If no player exists, display the corresponding message.
        """
        response = self.client.get(reverse("game:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no players in the world as of yet.")
        self.assertQuerySetEqual(response.context["player_list"], [])
    def test_with_player(self):
        """
        If a player exists, show its name on the screen.
        """
        player = Player.objects.create(name='John', health=100, hunger=15)
        response = self.client.get(reverse("game:index"))
        self.assertQuerySetEqual(
            response.context["player_list"],
            [player],
        )

# TODO: add tests for input form data once the user is given the opportunity to POST. See https://docs.djangoproject.com/en/5.1/intro/tutorial05/.
