from datetime import datetime

from rest_framework import serializers

from .models import Room, Reservation


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class ListCreateReservationSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    from_date = serializers.DateTimeField(required=True)
    to_date = serializers.DateTimeField(required=True)

    class Meta:
        model = Reservation
        fields = '__all__'

    def validate_meeting_room(self, value):
        # meeting room must be chosen
        if value is None:
            raise serializers.ValidationError(
                'please select a meeting room'
            )
        return value

    def validate(self, data):
        time_zone = data['from_date'].tzinfo

        # from_date must be later than now
        if data['from_date'] <= datetime.now(time_zone):
            raise serializers.ValidationError(
                'meeting must start in the future'
            )
        # from_date must be earlier than to_date
        if data['from_date'] >= data['to_date']:
            raise serializers.ValidationError(
                'meeting must start before it ends'
            )
        # validate that this meeting room is available on specified datetimes
        accepted_room_reservations = Reservation.objects.filter(
            meeting_room=data['meeting_room']
        )
        if any(
            True
            for reservation in accepted_room_reservations
            if (
                data['from_date'] <= reservation.from_date
                and data['to_date'] > reservation.from_date
            )
            or (
                data['from_date'] > reservation.from_date
                and data['from_date'] < reservation.to_date
            )
        ):
            raise serializers.ValidationError(
                'specified time frame is already reserved in this meeting room'
            )

        return data
