from django.forms import ModelForm 
from adopt.models import show

class SquirrelForm(ModelForm): 
    class Meta: 
        model = show 
        fields = '__all__'
