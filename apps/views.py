from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import AppForm
from .models import AppModel


# Create your views here.



def app_form(request):
    
    if request.method == 'POST':
     
        form = AppForm(request.POST, request.FILES)
        print(form.errors)

        if form.is_valid():
            form.save()
            print("VALID")

    form = AppForm()
    return render(request, 'apps/app_upload.html', {'form':form})

class AppView(DetailView):
    model = AppModel
    template_name = 'apps/app_page.html'
    context_object_name = 'apps'
    slug_url_kwarg = 'slug'

class AppListView(ListView):

    model = AppModel
    template_name = 'apps/homepage.html'
    context_object_name= 'apps_list'
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        app_data = self.model.objects.all()
        return app_data