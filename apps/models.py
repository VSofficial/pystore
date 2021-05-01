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
    version = models.FloatField(blank=True, null=True)
    developer = models.CharField(max_length=100, blank=True)
    app_py = models.FileField(upload_to='main/python')
    app_exe = models.FileField(upload_to='main/exe')
    icon = models.ImageField(upload_to='main/icons')

    def __str__(self):
        return self.appname

   


