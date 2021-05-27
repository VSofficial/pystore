from django.urls import path
from .views import app_form, AppView
from django.urls import reverse_lazy
from .models import AppModel
from apps import admin
from django.conf import settings
from django.conf.urls.static import static
app_name='apps'




urlpatterns = [
  #  path("r/", applicationpage, name='appx'),
    path("a/", app_form, name="appform"),
    path("b/<slug>", AppView.as_view(), name="appview"),
   # path("<str:appname>", AppDetailView.as_view(), name="appname" ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)