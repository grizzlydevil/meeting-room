from django.urls import path

from . import views

app_name = 'rooms'
urlpatterns = [
    path('create/', views.CreateRoomView.as_view(), name="rooms"),
    path('reservations/create/',
         views.CreateReservationView.as_view(),
         name="create_res"),
    path('reservations/cancel/<int:pk>/',
         views.CancelReservationView.as_view(),
         name="cancel_res"),
    path('reservations/<int:room>/<int:employee>/',
         views.RoomReservationsView.as_view(),
         name="room_filtered_res"),
    path('reservations/<int:room>/',
         views.RoomReservationsView.as_view(),
         name="room_res")
]
