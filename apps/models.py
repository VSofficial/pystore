from django.db import models
import re


# Create your models here.
'''
def get_matchname(a, b):
    """Returns the match name for a tag"""
    #return re.sub("\W+" , "", self.a, self.b)
    return (a+"/"+b)
'''

class AppModel(models.Model):
    appname = models.CharField(max_length=100)
    version = models.FloatField()
    developer = models.CharField(max_length=100)
    app_py = models.FileField(upload_to=developer)
    app_exe = models.FileField(upload_to=developer)
    icon = models.ImageField(upload_to=developer)

