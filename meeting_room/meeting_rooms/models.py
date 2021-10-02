from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=50)
    max_seats = models.PositiveSmallIntegerField(null=True, blank=True)
