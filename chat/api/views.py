from rest_framework.views import APIView
from rest_framework.request import Request
from chat.models import Message
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from chat.api.serializers import MessageSerializer
from django.core.exceptions import ObjectDoesNotExist


class MessageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request) -> Response:
        serializer: MessageSerializer = MessageSerializer(data=request.data)
        if not serializer.is_valid():
            response: Response = Response({"details": serializer.errors},
                                          status=status.HTTP_201_CREATED)
        else:
            message: Message = serializer.save(sender=request.user)
            response: Response = Response({"details": "message sent", "message_id": message.id},
                                          status=status.HTTP_201_CREATED)
        return response

    def get(self, request: Request) -> Response:
        message = Message.objects.order_by("sent_at").filter(is_read=False, receiver=request.user).first()
        if message is None:
            # the status is 400 to return another status
            response = Response({"details": "you have no unread messages"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            message.is_read = True
            message.save()
            message_serializer: MessageSerializer = MessageSerializer(message).data
            response = Response({"message": message_serializer}, status=status.HTTP_200_OK)
        return response

    def delete(self, request: Request, message_id: int) -> Response:
        try:
            message = Message.objects.get(id=message_id)
            if message.sender == request.user or message.receiver == request.user:
                message.delete()
                response: Response = Response({"details": "message deleted"},
                                              status=status.HTTP_200_OK)
            else:
                response: Response = Response({"details": "you cant delete other people messages"},
                                              status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            response: Response = Response({"details": f"message id {message_id} does not exist"},
                                          status=status.HTTP_400_BAD_REQUEST)
        return response


class MessagesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        if request.query_params.get("messages") == "unread":
            messages = Message.objects.filter(is_read=False, receiver=request.user).all()
        else:
            messages = Message.objects.filter(receiver=request.user).all()
        messages_serializer: MessageSerializer = MessageSerializer(messages, many=True).data
        response = Response({"messages": messages_serializer}, status=status.HTTP_200_OK)
        return response
