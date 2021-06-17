from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *
from django.http import request

class RecetaForm(ModelForm):
    #last_name = forms.CharField(blank=False)
    #first_name = forms.CharField(blank=False)
    class Meta:
        model = Receta
        fields = ['first_name','last_name','username','email']
    def __init__(self, *args, **kwargs):
        super(RecetaForm, self).__init__(*args, **kwargs)

    fields = ['basic_field']