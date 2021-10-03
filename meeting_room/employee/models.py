from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from authentication.models import CustomUser


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


@receiver(post_save, sender=Employee)
def update_permissions(sender, instance, created, **kwargs):
    if created:
        user = CustomUser.objects.get(pk=instance.user.pk)
        user.is_staff = True
        user.save()
