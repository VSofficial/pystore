from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic.detail import DetailView
from .forms import AppForm
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
    return render(request, 'apps/abcd.html', context=context)


def app_form(request):
    
    if request.method == 'POST':
     
        form = AppForm(request.POST, request.FILES)
        print(form.errors)

        if form.is_valid():
            form.save()
            print("VALID")

    form = AppForm()
    return render(request, 'apps/applicationpage.html', {'form':form})




'''
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)
'''
'''
def upload_app(request):
    if request.method == 'POST':
        form = AppForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard.html')
    else:
        form = AppForm()
    return render(request, 'upload_book.html', {
        'form': form
    })


class AppDetailView(DetailView):
    model = AppModel
    template_name = 'applicationpage.html'
    context_object_name = 'apps'

'''

'''
class UploadAppView(CreateView):
    model = AppModel
    form_class = AppForm
    success_url = reverse_lazy('class_book_list')
    template_name = 'upload_book.html'

'''