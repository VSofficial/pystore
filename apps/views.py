from django.shortcuts import render
from .models import AppModel
# Create your views here.
def applicationpage(request):
    context = {
        "app" : AppModel.appname,
        "version" : AppModel.version,
        "developer" : AppModel.developer,
        "py-file" : AppModel.app_py,
        "exe-file" : AppModel.app_exe,
        "icon" : AppModel.icon,
         }
    return render(request, 'apps/applicationpage.html', context=context)
