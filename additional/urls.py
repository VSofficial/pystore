from django.urls import path
from . import views

app_name = 'additional'

urlpatterns = [
    #path('apps/', api.app),
    path('notifications/', views.all_notifications, name='all_notifications'),
    path('info/', views.all_info, name="all_info" ),
    path('puzzle/', views.all_puzzle, name="all_puzzle" )
]


