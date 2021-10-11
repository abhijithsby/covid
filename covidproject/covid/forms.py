from django import forms
from django.forms import ModelForm

from covid.models import Movie

class MovieForm(ModelForm):
    class Meta:
        model= Movie
        fields=('name','address','Age','Phone')