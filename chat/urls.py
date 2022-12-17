from django.urls import path
from . import views

urlpatterns = [
    path('message', views.MessagesView.as_view())
]
