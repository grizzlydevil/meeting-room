from django.conf import settings
from django.db import models

from employee.models import Employee


class Room(models.Model):
    name = models.CharField(max_length=50)
    max_seats = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    title = models.CharField(max_length=160)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    employee = models.ManyToManyField(Employee)
    meeting_room = models.ForeignKey(
        Room, on_delete=models.CASCADE, blank=False, null=False
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.title}\nFrom: {self.from_date}\nTo: {self.to_date}'
