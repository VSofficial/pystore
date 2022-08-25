from django.urls import path
from .views import app_form, AppView, AppListView, app_form, SearchList
from django.urls import reverse_lazy
from .models import AppModel, AppStats, Comments, Issues
from apps import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetDoneView, PasswordResetView,
                                       PasswordResetCompleteView, PasswordResetConfirmView,
                                       PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetDoneView)
app_name='apps'




urlpatterns = [
  #  path("r/", applicationpage, name='appx'),
    path("upload/", app_form, name="appform"),
    path("upload_formset", app_form, name="appformset"),
    path("apps/<slug>", AppView.as_view(), name="appview"),
    path("home/", AppListView.as_view(), name="applist"),
    path("search/<str:inputValue>", SearchList, name="search"),
   # path("<str:appname>", AppDetailView.as_view(), name="appname" ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)