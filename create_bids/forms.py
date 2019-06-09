from django import forms
from .models import Bids


class BidForm(forms.ModelForm):
    Quote_amount = forms.IntegerField(required=True, min_value=1, label='Quote Amount(Ksh.)')
    Bid_description = forms.CharField(
        widget=forms.Textarea(
            attrs={'cols': 62, 'rows': 3}
        ),
        required=True,
        label='Bid Description'
    )

    class Meta:
        model = Bids
        fields = ('Bid_description', 'Quote_amount', 'Bid_documents_url')
