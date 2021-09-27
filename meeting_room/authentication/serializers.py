from rest_framework import serializers

from .models import User


class CustomUser(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')
        

