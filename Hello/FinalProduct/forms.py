from django import forms
from .models import *


class CreateProduct(forms.ModelForm):
    class Meta:
        model = Finalproduct
        fields = [
            'name',
        ]


class CreateComponent(forms.ModelForm):
    class Meta:
        model = Components
        fields = [
            'Part_name', 'Part_Number', 'Primary_Stock_Unit',
            'Purchase_Stock_Unit', 'Material', 'type_of_production', 'cost',
            'document', 'Cheack_for_Allocation'

        ]


class CreateProcess(forms.ModelForm):
    class Meta:
        model = Process
        fields = [
            'name'
        ]


class CreateRawMaterial(forms.ModelForm):
    class Meta:
        model = RawMaterial
        fields = '__all__'


class CreateRawMaterial_Record(forms.ModelForm):
    class Meta:
        model = RawMaterial
        fields = '__all__'


class ProcessForm(forms.Form):
    OPTIONS = (
        ("Cutting", "Cutting"),
        ("Milling", "Milling"),
        #  ("NLD", "Neitherlands"),
    )
    Process = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                        choices=OPTIONS)
