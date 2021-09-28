from rest_framework import serializers

from dj_rest_auth.serializers import UserDetailsSerializer

from .models import User


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class UserSerializer(UserDetailsSerializer):
    user_serializer = CustomUserSerializer()


    class Meta(UserDetailsSerializer.Meta):
        fields = user_serializer.Meta.fields
