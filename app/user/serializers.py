"""
Serializers for the user API view
"""
from django.contrib.auth import (
    get_user_model,
    authentificate,
)
from django.utils.translation import gettext as _

from rest_framework import serializers

# (user serializer, modelserializer) 
class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""

    class Meta:
        model =get_user_model()
        fields = ['email', 'password', 'name']
        # User can write but pw cannot be returned.
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    # This part will be only called when validation is successful
    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)

class AuthTokenSerializer(serializer.Serializer):
    """Serializer for the user auth token."""
    email = serializers.EmailField()
    password = serializers.Charfield(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )
    
    def validate(self, attrs):
        """Validate and authenticate the user."""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('resquest'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credencials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

