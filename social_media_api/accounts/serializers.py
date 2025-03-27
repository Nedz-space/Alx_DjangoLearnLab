from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        """Create and return a new user with a hashed password."""
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user  # Return only the user instance, not a dictionary


class UserSerializer(serializers.ModelSerializer):
    """Serializer for retrieving user details."""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']


class LoginSerializer(serializers.Serializer):
    """Serializer for user authentication (login)."""
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def validate(self, data):
        """Authenticate the user and return their token."""
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid username or password.")

        token, created = Token.objects.get_or_create(user=user)
        return {"token": token.key, "user": UserSerializer(user).data}  # Ensure return statement

