from abc import ABC

from rest_framework import serializers


class RegisterSerializer(serializers.Serializer, ABC):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(min_length=8)


class LoginSerializer(RegisterSerializer, ABC):
    """Login serializer."""
