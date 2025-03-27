from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user model, handling user registration."""
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        """Create and return a new user with a hashed password and generate an auth token."""
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        # Create an authentication token for the newly created user
        token = Token.objects.create(user=user)
        return {"user": user, "token": token.key}


class LoginSerializer(serializers.Serializer):
    """Serializer for user authentication (login)."""
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def validate(self, data):
        """Authenticate the user and return their token."""
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid username or password.")
        
        # Retrieve or create an authentication token
        token, created = Token.objects.get_or_create(user=user)
        return {"token": token.key, "user": UserSerializer(user).data}

