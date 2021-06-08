from django.forms import ModelForm
from .models import AppModel


class AppForm(ModelForm):
  class Meta:
   model = AppModel
   fields = ['appname', 'version', 'developer', 'app_py', 'app_exe', 'icon', 'description', 'screenshots', 'requirement', 'category']
         
  


'''
class ApplicationForm(forms.Form):
        form_field1 = forms.CharField(max_length=40, required=True)
        form_field2 = forms.CharField(max_length=60, required=False)
'''