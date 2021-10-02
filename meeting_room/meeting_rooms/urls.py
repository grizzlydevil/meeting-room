from django.urls import path

from . import views

app_name = 'rooms'
urlpatterns = [
    path('create/', views.CreateRoomView.as_view(), name="rooms"),
]
