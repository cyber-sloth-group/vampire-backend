from django.db import models
from django.utils import timezone

from users.models import User


class Heart(models.Model):
    measured_datetime = models.DateTimeField(default=timezone.now())
    sys = models.IntegerField(default=0)
    dia = models.IntegerField(default=0)
    heart_rate = models.IntegerField(default=0)
    note = models.TextField(null=True)
    created = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        ordering = ['measured_datetime']
