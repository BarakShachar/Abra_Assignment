from rest_framework import serializers
from chat.models import Message


class MessageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['sender', 'subject', 'message', 'receiver']


class MessageSerializer(serializers.ModelSerializer):
    sent_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Message
        fields = ['uuid', 'sent_at', 'sender', 'subject', 'message']
