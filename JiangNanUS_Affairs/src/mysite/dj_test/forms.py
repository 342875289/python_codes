from django import forms
from django.forms import ModelForm
from .models import Person
from django.utils.translation import ugettext_lazy as _


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name',max_length=100)
    your_age = forms.IntegerField(label='Your age')
    
class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name','age','birth_date']
        labels = {
            'first_name': _('Writer_first_name'),
        }
        help_texts = {
            'first_name': _('Some useful help text.'),
        }
        error_messages = {
            'first_name': {
                'max_length': _("This writer's name is too long."),
            },
        }
        
