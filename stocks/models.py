
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.hashers import make_password

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')

class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    description = models.TextField()
    rs = models.FloatField()
    rv = models.FloatField()
    ci = models.FloatField()
    rt = models.FloatField()
    grt = models.FloatField()
    sales = models.FloatField()
    ey_percentage = models.FloatField()

    def __str__(self):
        return self.ticker
class UserPassword(models.Model):
    password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.pk:  # Only hash the password if it's a new record
            self.password = make_password(self.password)
        super().save(*args, **kwargs)