from django import forms
from .models import Farmer

class Farmerform(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = [
            'name',
            'address',
            'contact',
            'age',
            'item' 
        ]