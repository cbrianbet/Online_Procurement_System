from django import forms
from .models import *


class BidForm(forms.ModelForm):
    Quote_amount = forms.IntegerField(required=True, min_value=1, label='Quote Amount(Ksh.)')
    Bid_description = forms.CharField(
        widget=forms.Textarea(
            attrs={'cols': 62, 'rows': 3}
        ),
        required=True,
        label='Bid Specifications'
    )

    class Meta:
        model = Bids
        fields = ('Bid_description', 'Quote_amount')


class DesktopBidForm(forms.ModelForm):
    Quote_amount = forms.IntegerField(required=True, min_value=1, label='Quote Amount per Item(Ksh.)')
    Product = forms.CharField(required=True)
    Processor = forms.CharField(required=True)
    Memory = forms.CharField(required=True)
    Operating_system = forms.CharField(required=True)
    Graphics = forms.CharField(required=True)
    Storage = forms.CharField(required=True)

    class Meta:
        model = DesktopBid
        fields = (
            'Product',
            'Processor',
            'Memory',
            'Operating_system',
            'Storage',
            'Graphics',
            'Quote_amount',
            'Bid_documents_url'
        )
