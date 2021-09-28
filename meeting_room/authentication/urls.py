from django.urls import path, include

from . import views

app_name = 'auth'
urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('me/', views.UserDetailView.as_view())
]
