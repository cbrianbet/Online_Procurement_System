from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import AcceptForm
from create_bids.models import Bids
from django.http import Http404

from create_bids.models import Bids


@login_required
def bid_for_tender_list(request, bid_id):
    context = {
        'bids': Bids.objects.filter(Tender_ID_id=bid_id)
    }
    return render(request, 'approve_bids/tenderBid.html', context)


def accept_bid(request, b_id):
    bid = Bids.objects.get(pk=b_id)
    if request.method == "POST":
        form = AcceptForm(request.POST)
        if form.is_valid():
            abid = form.save(commit=False)
            abid.bid_ID = bid
            abid.save()
        context = {
            'form': form
        }
        return render(request, 'approve_bids/Bidupdate.html', context)
