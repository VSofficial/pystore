from django.forms import ModelForm
from .models import AppModel, Screenshots


class AppForm(ModelForm):
  class Meta:
   model = AppModel
   fields = ['appname', 'version', 'developer', 'app_py', 'app_exe', 'icon', 'description', 'requirement', 'category']
         
  
class ScreenshotForm(ModelForm):
        class Meta:
                model = Screenshots
                fields = ['image', 'app']


'''
class ApplicationForm(forms.Form):
        form_field1 = forms.CharField(max_length=40, required=True)
        form_field2 = forms.CharField(max_length=60, required=False)
'''