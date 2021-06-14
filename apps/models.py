from django.utils.text import slugify
from django.db import models
import re
import datetime
from authapp.models import UserRegistrationModel
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
    app_py = models.FileField(upload_to='python')
    app_exe = models.FileField(upload_to='exe')
    icon = models.ImageField(upload_to='icons')
    slug = models.SlugField(unique=True, default='default')
    description = models.TextField(default="No description by publisher", null=True)
    screenshots = models.ImageField(upload_to='screenshots', null=True)
    requirement = models.CharField(blank=True, null=True, max_length=50)
    update_date =models.DateField(auto_now=True)

    CATEGORY_CHOICE = (
    ('ML', "Machine Learning"),
    ('BIGDATA', "Big Data"),
    ('AUTOMATION', "Automation"),
    ('OPENCV', "Image/Video Processing"),
    ('PRODUCTIVITY', "Productivity / Office Tools"),
    ('DATASCIENCE', "Data Science"),
    ('DRIVERS', "Drivers/Database/System Programs"),
    ('DATAPROCESSING', "Data Processing"),
    ('MISC', "Others"),
     )
     
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICE, default='MISC')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.appname+self.developer)
        super(AppModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.appname

'''
class UserRating(models.Model):
    rating = models.FloatField(blank=True, null=True, max_length=10.0)
    user = models.ForeignKey(UserRegistrationModel, on_delete=models.CASCADE)
'''
 
class Comments(models.Model):
    comment = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(UserRegistrationModel, on_delete=models.CASCADE)
    app = models.ForeignKey(AppModel, on_delete=models.CASCADE)

class Issues(models.Model):
    issue = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    screenshots = models.ImageField(upload_to='issues', null=True)


class AppStats(models.Model):
    total_downloads = models.IntegerField(default=0)
    total_ratings = models.IntegerField(default=0)
    download_size_py = models.IntegerField(default=0)
    download_size_windows = models.IntegerField(default=0)
    app = models.ForeignKey(AppModel, on_delete=models.CASCADE)

    
