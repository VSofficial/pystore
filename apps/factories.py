import factory 
import factory.django
from .models import AppModel

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
