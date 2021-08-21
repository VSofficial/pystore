from django.db import models
from django.forms import inlineformset_factory
from .models import AppModel, Screenshots
from .forms import AppForm
 
AppFormset = inlineformset_factory(AppModel, Screenshots, fields=('app',), form=AppForm)

