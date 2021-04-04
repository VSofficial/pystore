from django.urls import path
from .views import applicationpage
from django.urls import reverse_lazy
from .models import AppModel

app_name='apps'




urlpatterns = [
    path("r/", applicationpage, name='appx'),
]
