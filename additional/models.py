from django.db import models

# Create your models here.
class Notifications(models.Model):
    title = models.TextField(max_length=254, null=True, blank=True)
    subTitle = models.TextField(max_length=128, null=True, blank=True)
    icon = models.ImageField(null=True, blank=True)
    time_frame = models.DateTimeField(auto_now=True)