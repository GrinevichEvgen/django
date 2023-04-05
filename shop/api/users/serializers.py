from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(min_length=8)


class LoginSerializer(RegisterSerializer):
    """Login serializer."""


class LogoutSerializer(serializers.Serializer):
    pass
