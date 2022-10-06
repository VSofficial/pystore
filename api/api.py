from rest_framework import serializers
from apps.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view


class AppsSerializers(serializers.ModelSerializer):
    class Meta:
        model = AppModel
        fields = "__all__"



@csrf_exempt
def app_details(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        app = AppModel.objects.get(pk=pk)
    except app.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AppsSerializers(app)
        return JsonResponse(serializer.data)




@api_view(['GET'])
@csrf_exempt
def all_apps(request):
    apps = AppModel.objects.all()
    serializer = AppsSerializers(apps, many =True)
    return JsonResponse(serializer.data, safe=False)