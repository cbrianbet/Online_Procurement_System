from django import forms
from .models import Bids


class BidForm(forms.ModelForm):
    Quote_amount = forms.IntegerField(required=True, min_value=1, label='Quote Amount')
    Bid_description = forms.CharField(
        widget=forms.Textarea(
            attrs={'cols': 62, 'rows': 3}
        ),
        required=True,
        label='Bid Description'
    )
    Bid_documents_url = forms.FileField(required=False, label='Upload documents for Bid')

    class Meta:
        model = Bids
        fields = ('Bid_description', 'Quote_amount', 'Bid_documents_url')
