from datetime import datetime
from rest_framework.views import APIView
from rest_framework.request import Request
from chat.models import Messages
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


class MessagesView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request) -> Response:
        sender: User = request.user
        subject: str = request.data["subject"]
        message: str = request.data["message"]
        receiver: User = User.objects.get(pk=2)
        message_ser: Messages = Messages.objects.create(sender=sender,
                                                        subject=subject,
                                                        message=message,
                                                        receiver=receiver,
                                                        creation_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        response: Response = Response({"message": "message sent"}, status=status.HTTP_200_OK)
        return response
