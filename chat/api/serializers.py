from rest_framework import serializers
from chat.models import Message


class MessageSerializer(serializers.ModelSerializer):
    sent_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sent_at', 'sender', 'subject', 'message', 'receiver']
        read_only_fields = ['sender']
