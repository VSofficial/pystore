from django.db import models
import re
import factory 
import factory.django

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

class AppFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = AppModel

    name = factory.Faker('name')
    address = factory.Faker('address')
    phone_number = factory.Faker('phone_number')
    appname = factory.Faker('appname')
    version = factory.Faker('version')
    developer = factory.Faker('developer')
    app_py = factory.Faker('app_py')
    app_exe = factory.Faker('app_exe')
    icon = factory.Faker('icon')
