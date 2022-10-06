from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import AppForm
from django.contrib.auth.decorators import login_required
#from .formsets import AppFormset
from .models import AppModel, Issues, AppStats, Comments, Rating
from django.db.models import Sum
from django.http import JsonResponse
from django.forms.models import model_to_dict

from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@login_required
def app_form(request):
    
    if request.method == 'POST':
     
        form = AppForm(request.POST, request.FILES)
        print(form.errors)

        if form.is_valid():
            form.save()
            print("VALID")
        

    form = AppForm()
    return render(request, 'apps/app_upload.html', {'form':form})




def apps_and_comments(request):

    rating_obj = Rating.objects.all()
    avg_rating = Rating.objects.aggregate(total_rating=Sum('rating'))
    avgr = avg_rating['total_rating'] / 2


    return {'context_appmodel': AppModel.objects.all(),
            'context_comments': Comments.objects.all(),
            'context_rating': avgr}


class AppView(DetailView):
    model = AppModel
    model_comments = Comments
    template_name = 'apps/app_page.html'
    context_object_name = 'apps'
    slug_url_kwarg = 'slug'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['issues'] = Issues.objects.all()
        context['stats'] = AppStats.objects.all()
        context['comments'] = Comments.objects.all()
        return context




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

@csrf_exempt
def SearchList(request):
    if request.method == 'GET':
        ski = request.GET.get('inputValue')
        search_text="notes"
        #search_text="notes"
        if ski==None:
            ski="notes"

        mydata = AppModel.objects.all().filter(appname__contains=ski).values_list()
        #list1 = queryset_to_dict(mydata)
        data_obj = {'response': list(mydata)}
        print(ski)
        if mydata.exists():
            print(mydata)
            return JsonResponse(data_obj)
            
        else: return JsonResponse("not working")




