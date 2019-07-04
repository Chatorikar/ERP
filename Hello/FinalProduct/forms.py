from django import forms
from .models import *



class CreateProduct(forms.ModelForm):
    class Meta:
        model = Finalproduct
        fields = '__all__'

class CreateComponent(forms.ModelForm):
    class Meta:
        model = Components
        fields = '__all__'


class CreateProcess(forms.ModelForm):
    class Meta:
        model = Process
        fields = '__all__'