from rest_framework import serializers
from additional.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import render




class NotificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = "__all__"

