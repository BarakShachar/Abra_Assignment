from rest_framework import serializers
from chat.models import Message
from django.contrib.auth.models import User


class MessageCreateSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username"
    )
    receiver = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username"
    )

    class Meta:
        model = Message
        fields = ['uuid', 'sender', 'subject', 'message', 'receiver', 'creation_date']


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username"
    )

    class Meta:
        model = Message
        fields = ['uuid', 'creation_date', 'sender', 'subject', 'message']