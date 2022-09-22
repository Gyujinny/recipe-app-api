"""
Views for the user API
"""
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_setting

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)

class CreateUserview(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class CreateTokenview(ObtainAuthToken):
    """Create a new user in the system."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_setting.DEFAULT_RENDERER_CLASSES
