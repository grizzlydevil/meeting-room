from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .serializers import RoomSerializer, ListCreateReservationSerializer,\
                         ReservationSerializer
from .models import Reservation
from employee.models import Employee


class CreateRoomView(generics.CreateAPIView):
    permission_classes = (IsAdminUser, IsAuthenticated)
    serializer_class = RoomSerializer


class CreateReservationView(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser, IsAuthenticated)
    queryset = Reservation.objects.all()
    serializer_class = ListCreateReservationSerializer

    def get_queryset(self):
        employee = Employee.objects.get(user=self.request.user)
        return self.queryset.filter(employee=employee)


class CancelReservationView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAdminUser, IsAuthenticated)
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class RoomReservationsView(generics.ListAPIView):
    permission_classes = (IsAdminUser, IsAuthenticated)
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        room_reservations = self.queryset.filter(
            meeting_room=self.kwargs['room']
        )
        employee = self.kwargs.get('employee')
        if employee:
            room_reservations = room_reservations.filter(employee=employee)
        return room_reservations
