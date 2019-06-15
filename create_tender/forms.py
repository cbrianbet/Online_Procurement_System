from django import forms
from .models import *


class CreateTenderForm(forms.ModelForm):
    choice = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    tender_title = forms.CharField(required=True)
    tender_desc = forms.CharField(
        widget=forms.Textarea(
            attrs={'cols': 62, 'rows': 3}
        ),
        label='Tender specifications'
    )
    tender_duration = forms.IntegerField(required=True, help_text='(in months)')
    is_active = forms.ChoiceField(required=True, choices=choice, label="Is the tender active?")

    class Meta:
        model = Tender
        fields = ('tender_title', 'tender_desc', 'tender_duration', 'is_active')


class DesktopTenderForm(forms.ModelForm):
    Product = forms.CharField(required=True)
    Processor = forms.CharField(required=True)
    Memory = forms.CharField(required=True)
    Operating_system = forms.CharField(required=True)
    Graphics = forms.CharField(required=True)
    Storage = forms.CharField(required=True)
    Quantity = forms.IntegerField(required=True, min_value=1)

    class Meta:
        model = Desktop_Tender
        fields = ('Product', 'Processor', 'Memory', 'Operating_system', 'Storage', 'Graphics', 'Quantity')


class ConstTenderForm(forms.ModelForm):
    choice = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    Mod = forms.CharField(required=True, label='Model')
    Net_power = forms.CharField(required=True)
    Electric = forms.ChoiceField(required=True, choices=choice)
    Engine = forms.CharField(required=True)
    Operating_weight = forms.CharField(required=True)
    Certification = forms.CharField(required=True)
    Quantity = forms.CharField(required=True)

    class Meta:
        model = ConstructionTender
        fields = ('Mod', 'Net_power', 'Electric', 'Engine', 'Operating_weight', 'Certification', 'Quantity')


class FurnitureTenderForm(forms.ModelForm):
    Product = forms.CharField(required=True)
    Dimensions = forms.CharField(required=True, help_text='(Length x Width x Height)cm')
    Material = forms.CharField(required=True)
    Color = forms.CharField(required=True)
    Quantity = forms.CharField(required=True)

    class Meta:
        model = FurnitureTender
        fields = ('Product', 'Dimensions', 'Color', 'Material', 'Quantity')
