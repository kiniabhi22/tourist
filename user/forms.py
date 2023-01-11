from django import forms
from django.forms import ModelForm #to use all attributes from model
from .models import City #to use the class City fields

class AddCityForm(ModelForm):
    class Meta:
        model=City
        #fields="__all__" #if we want ton add
        fields=('name','desc','days','cost','offer','image')
        widgets={
            'name':forms.TextInput(attrs={'class':'myname','placeholder':'Enter'})

        
        }

