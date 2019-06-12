import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404

from .models import AcceptBid
from django.contrib import messages
from create_bids.models import Bids
from create_tender.models import Tender


@login_required
def bid_for_tender_list(request, bid_id):
    context = {
        'bids': Bids.objects.filter(Tender_ID_id=bid_id)
    }
    return render(request, 'approve_bids/tenderBid.html', context)


@login_required
def accept_bid(request, b_id):
    bid = Bids.objects.get(pk=b_id)
    if request.method == "POST":
        bids = AcceptBid(bid_ID=bid, date=datetime.datetime.now().date())
        bids.save()
        bids = Tender()
        bids.tender_award = "Yes"
        bids.save()
        messages.success(request, f"Bid by {bid.user.profile.company_name} for {bid.Tender_ID.tender_title} accepted")
        return redirect('tender_history')


@login_required
def bid_info(request, bid):
    bid = Bids.objects.get(pk=bid)
    context = {
        'bid': bid
    }
    return render(request, "approve_bids/bidslist.html", context)
