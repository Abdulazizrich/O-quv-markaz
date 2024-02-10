from django import forms
from .models import *



class YonalishForm(forms.Form):
    nom=forms.CharField(label='Nom:')
    narx = forms.IntegerField(label='Narx:')

class XonaForm(forms.Form):
    nom=forms.CharField(label='Nom:')
    raqam = forms.IntegerField(label='Raqam:')

class UstozForm(forms.ModelForm):
    class Meta:
        model=Ustoz
        fields='__all__'

class GuruhForm(forms.ModelForm):
    class Meta:
        model=Guruh
        fields='__all__'

class OquvchiForm(forms.ModelForm):
    class Meta:
        model=Oquvchi
        fields='__all__'


