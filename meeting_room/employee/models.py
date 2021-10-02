from django.db import models
from django.conf import settings


class Employee(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    job_title = models.CharField(max_length=50, null=False, blank=False)
    first_name = models.CharField(max_length=60, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    date_started = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
