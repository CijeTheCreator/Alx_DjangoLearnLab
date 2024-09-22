from rest_framework import serializers
from notifications.models import Notification
from rest_framework.authtoken.models import Token

class NotificationSerializer(serializers.ModelSerializer):
    recipient_username = serializers.CharField(source='recipient.username', read_only=True)
    actor_username = serializers.CharField(source='actor.username', read_only=True)
    verb = serializers.CharField(max_length=255)

    class Meta:
        model = Notification
        fields = ['id', 'recipient_username', 'actor_username', 'verb', 'timestamp']
        read_only_fields = ['id', 'timestamp']

    def create(self, validated_data):
        # Using objects.create from Token to create a notification if needed
        return Notification.objects.create(**validated_data)
