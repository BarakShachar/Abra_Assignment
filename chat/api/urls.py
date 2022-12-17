from django.urls import path
from chat.api import views

urlpatterns = [
    path('message/', views.MessageView.as_view()),
    path('message/<message_uuid>/', views.MessageView.as_view()),
    path('messages/', views.MessagesView.as_view()),
]
