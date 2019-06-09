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
        help_text='Describe the tender',
        label='Tender Description'
    )
    tender_duration = forms.IntegerField(required=True, help_text='(in months)')
    is_active = forms.ChoiceField(required=True, choices=choice, label="Is the tender active?")
    tender_value = forms.IntegerField(required=False, min_value=1, label="Value of tender")
    # TODO widgets Boolean fields

    class Meta:
        model = Tender
        fields = ('tender_title', 'tender_desc', 'tender_duration', 'tender_value', 'is_active')
