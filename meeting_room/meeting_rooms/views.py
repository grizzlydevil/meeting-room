from rest_framework import generics

from .serializers import RoomSerializer


class CreateRoomView(generics.CreateAPIView):
    serializer_class = RoomSerializer
