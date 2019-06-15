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


class FurnitureBidForm(forms.ModelForm):
    Quote_amount = forms.IntegerField(required=True, min_value=1, label='Quote Amount per Item(Ksh.)')
    Product = forms.CharField(required=True)
    Color = forms.CharField(required=True)
    Dimensions = forms.CharField(required=True)
    Material = forms.CharField(required=True)

    class Meta:
        model = FurnitureBid
        fields = (
            'Product',
            'Material',
            'Dimensions',
            'Color',
            'Quote_amount',
            'Bid_documents_url'
        )


class ConstructionBidForm(forms.ModelForm):
    choice = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    Quote_amount = forms.IntegerField(required=True, min_value=1, label='Quote Amount per Item(Ksh.)')
    Mod = forms.CharField(required=True, label='Model')
    Engine = forms.CharField(required=True)
    Certification = forms.CharField(required=True)
    Electric = forms.ChoiceField(required=True, choices=choice)
    Operating_weight = forms.CharField(required=True)
    Net_power = forms.CharField(required=True)

    class Meta:
        model = ConstructionBid
        fields = (
            'Mod',
            'Engine',
            'Electric',
            'Operating_weight',
            'Certification',
            'Net_power',
            'Quote_amount',
            'Bid_documents_url'
        )
