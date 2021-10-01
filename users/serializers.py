from abc import ABC

from django.contrib.auth import authenticate
from rest_framework import serializers

from users.models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])

        if not user:
            raise serializers.ValidationError('Incorrect email or password')

        if not user.is_active:
            raise serializers.ValidationError('User is not active')

        return {'user': user}


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password'
        )
        extra_kwargs = {
            'password': {'required': True, 'write_only': True},
            'username': {'required': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(
            validated_data.pop('username'),
            validated_data.pop('password'),
            **validated_data
        )
