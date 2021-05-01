from django.forms import ModelForm
from apps.models import AppModel


class AppForm(ModelForm):
     class Meta:
         model = AppModel
         fields = ['pub_date', 'headline', 'content', 'reporter']
         widgets = {
            'name': TextInput(),
            'description': Textarea(attrs={'cols':80},'rows':20)
        }

 form = AppForm()

 app = AppModel.objects.get(pk=1)
 form = AppForm(instance=app)