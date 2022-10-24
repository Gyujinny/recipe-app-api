"""
Tests for recipe APIs.
"""
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe

from recipe.serializers import RecipeSerializer

RECIPE_URL = reverse('recipe:recipe-list')

def create_recipe(user, **params):
    """Create and retuen a sample recipe."""
    defaults = {
        'title': 'Sample recipe title',
        'time_minutes': 22,
        'price': Decimal(''),
        'decription': 'Sample description',
        'link': 'http://example.com/recipe.pdf',
    }
    defualts.update(params)

    recepe = Recipe.objects.create(user=user, **defaults)
    return recipe


class PublicRecipeAPITests(TestCase):
    """Test unauthentificated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API."""
        res = self.client.get(RECIPE_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateRecipeApiTests(TestCase):
    """Test authentificated API requests."""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'user@example.com',
            'testpass123',
        )

    def test_retrive_recipes(self):
        """Test retrieving a list of recipes."""
        create_recipe(user=self.user)
        create_recipe(user=self.user)

        res = self.client.get(RECIPE_URL)

        recipes = Recipe.objects.all().order_by('-id')
        serializer = RecipeSerializer(recipes, many=True)
        self.asserEqual(res.status_code, status.HTTP_200_OK)
        self.asserEqual(res.data, serializer.data)

    def test_recipe_list_linited_to_user(self):
        """Test list of recipes is limited to authenticated user."""
        other_user = get_user_mode().objects.create_user(
            'other@example.com',
            'password123',
        )
        create_recipe(user=other_user)
        create_recipe(user=self.user)

        res = self.client.get(RECIPE_URL)

        recipes = Recipe.objects.filter(user=self.user)
        serializer = RecipeSerializer(recipes, many=True)
        self.asserEqual(res.status_code, status.HTTP_200_OK)
        self.asserEqual(res.data, serializer.data)


