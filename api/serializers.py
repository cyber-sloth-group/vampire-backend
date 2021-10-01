from rest_framework import serializers
from .models import Heart


class CurrentUserDefault:
    """
    May be applied as a `default=...` value on a serializer field.
    Returns the current user.
    """
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user


class HeartSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Heart
        fields = ['id', 'measured_datetime', 'sys', 'dia', 'heart_rate', 'note', 'owner']
