from rest_framework import serializers
from additional.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view



class NotificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = "__all__"

class InfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"

class PuzzleGameSerializers(serializers.ModelSerializer):
    class Meta:
        model = PuzzleGame
        fields = "__all__"



@api_view(['GET'])
@csrf_exempt
def all_notifications(request):
    n = Notifications.objects.all()
    serializer = NotificationSerializers(n, many =True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@csrf_exempt
def all_info(request):
    n = Info.objects.all()
    serializer = InfoSerializers(n, many =True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@csrf_exempt
def all_puzzle(request):
    n = PuzzleGame.objects.all()
    serializer = PuzzleGameSerializers(n, many =True)
    return JsonResponse(serializer.data, safe=False)
