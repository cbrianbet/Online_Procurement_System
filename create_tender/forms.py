from django import forms
from .models import Tender


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
