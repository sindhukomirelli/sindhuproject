from django import forms
from sindhumodelapp.models import Worldcup

class Worldcupform(forms.ModelForm):
    class Meta:
        model=Worldcup
        fields='__all__'
