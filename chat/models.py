from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Message(models.Model):
    uuid = models.UUIDField(blank=False, unique=True, primary_key=True)
    sender = models.ForeignKey(
        User,
        related_name="message_sender",
        blank=False,
        on_delete=models.CASCADE
    )
    subject = models.CharField(max_length=255, blank=False)
    message = models.CharField(max_length=2048, blank=False)
    receiver = models.ForeignKey(
        User,
        related_name="message_receiver",
        blank=False,
        on_delete=models.CASCADE
    )
    creation_date = models.DateTimeField(blank=False)
    is_read = models.BooleanField(default=False, blank=False)
