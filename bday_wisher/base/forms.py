from django.forms import ModelForm
from .models import Bday

#Auto form builder 
#Builds the forms to be displayed on the site
class BdayForm(ModelForm):
    class Meta:
        model=Bday
        fields='__all__'