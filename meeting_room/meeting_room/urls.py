from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls', namespace='auth')),
    path('employee/', include('employee.urls', namespace='employee')),
    path('rooms/', include('meeting_rooms.urls', namespace='rooms'))
]
