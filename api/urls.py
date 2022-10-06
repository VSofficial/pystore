from django.urls import path
from . import api

app_name = 'api'

urlpatterns = [
    #path('apps/', api.app),
    path('apps/<int:pk>/', api.app_details, name='api'),
    path('all/', api.all_apps, name='all_api')
]