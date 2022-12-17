import uuid
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.request import Request
from chat.models import Message
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from chat.serializers import MessageCreateSerializer, MessageSerializer


class MessageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request) -> Response:
        sender: User = request.user
        data = dict(request.data)
        data["sender"] = sender.username
        data["creation_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        data["uuid"] = uuid.uuid4()
        serializer: MessageCreateSerializer = MessageCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        message: Message = serializer.save()
        response: Response = Response({"details": "message sent", "message_uuid": message.uuid},
                                      status=status.HTTP_200_OK)
        return response

    def get(self, request: Request) -> Response:
        message = Message.objects.filter(is_read=False, receiver=request.user).first()
        if message is not None:
            message.is_read = True
            message.save()
            message_serializer: MessageSerializer = MessageSerializer(message).data
            response = Response({"message": message_serializer}, status=status.HTTP_200_OK)
        else:
            response = Response({"details": "you have no unread messages"}, status=status.HTTP_400_BAD_REQUEST)
        return response

    def delete(self, request: Request, message_uuid: uuid) -> Response:
        try:
            Message.objects.get(uuid=message_uuid).delete()
            response: Response = Response({"details": "message deleted"},
                                          status=status.HTTP_200_OK)
        except Message.DoesNotExist:
            response: Response = Response({"details": f"message uuid {message_uuid} does not exist"},
                                          status=status.HTTP_400_BAD_REQUEST)
        return response


class MessagesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        if request.query_params.get("unread"):
            messages = Message.objects.filter(is_read=False, receiver=request.user).all()
        else:
            messages = Message.objects.filter(receiver=request.user).all()
        messages_serializer: MessageSerializer = MessageSerializer(messages, many=True).data
        response = Response({"messages": messages_serializer}, status=status.HTTP_200_OK)
        return response
