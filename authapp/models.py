from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class UserRegistrationModel(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    
    def __str__(self):
            return self.user.username

  