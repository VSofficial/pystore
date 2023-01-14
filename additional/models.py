from django.db import models

# Create your models here.
class Notifications(models.Model):
    title = models.TextField(max_length=254, null=True, blank=True)
    subTitle = models.TextField(max_length=128, null=True, blank=True)
    icon = models.ImageField(null=True, blank=True)
    time_frame = models.DateTimeField(auto_now=True)


class Info(models.Model):
    title = models.TextField(max_length=254, null=True, blank=True)
    distance = models.TextField(max_length=128, null=True, blank=True)


class PuzzleGame(models.Model):
    timer = models.IntegerField(max_length=5, default=30)
    win_state = models.TextField(max_length=256, null=True, blank=True)
    lose_state = models.TextField(max_length=256, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    @classmethod
    def object(cls):
        return cls._default_manager.all().first() # Since only one item

    def save(self, *args, **kwargs):
        self.pk = self.id = 1
        return super().save(*args, **kwargs)

