from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Message(models.Model):
    sender = models.ForeignKey(
        User,
        related_name="message_sender",
        blank=False,
        on_delete=models.CASCADE,
        to_field="username"
    )
    subject = models.CharField(max_length=255, blank=False, null=False)
    message = models.CharField(max_length=2048, blank=False, null=False)
    receiver = models.ForeignKey(
        User,
        related_name="message_receiver",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        to_field="username"
    )
    sent_at = models.DateTimeField(blank=False, null=False, default=now)
    is_read = models.BooleanField(default=False, blank=False, null=False)
