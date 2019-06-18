import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse

from .models import *
from core.models import *
from django.contrib import messages
from create_bids.models import FurnitureBid, DesktopBid, ConstructionBid
from create_tender.models import *


@login_required
def bid_for_tender_list(request, bid_id):
    bids = DesktopBid.objects.filter(Tender_ID_id=bid_id)
    context = {
        'bids': bids
    }
    return render(request, 'approve_bids/tenderBid.html', context)


@login_required
def bid_furn_tender_list(request, bid_id):
    bids = FurnitureBid.objects.filter(Tender_ID_id=bid_id)
    context = {
        'fbids': bids
    }
    return render(request, 'approve_bids/furnTenderBid.html', context)


@login_required
def bid_const_tender_list(request, tender_id):
    bids = ConstructionBid.objects.filter(Tender_ID_id=tender_id)
    context = {
        'cbids': bids
    }
    return render(request, 'approve_bids/constTenderBid.html', context)


@login_required
def accept_bid(request, b_id):
    bid = DesktopBid.objects.get(pk=b_id)
    if request.method == "POST":
        bids = AcceptBid()
        bids.bid_ID = bid
        bids.date = datetime.datetime.now().date()
        bids.save()
        bids = Desktop_Tender.objects.filter(pk=bid.Tender_ID_id).update(tender_award='Yes')

        messages.success(request, f"Bid by {bid.user.profile.company_name} for {bid.Tender_ID.Product} accepted")
        return redirect('tender_history')


@login_required
def accept_furn_bid(request, b_id):
    bid = FurnitureBid.objects.get(pk=b_id)
    if request.method == "POST":
        bids = AcceptFurnBid()
        bids.bid_ID = bid
        bids.date = datetime.datetime.now().date()
        bids.save()
        bids = FurnitureTender.objects.filter(pk=bid.Tender_ID_id).update(tender_award='Yes')
        messages.success(request, f"Bid by {bid.user.profile.company_name} for {bid.Tender_ID.Product} accepted")
        return redirect('tender_history')


@login_required
def accept_const_bid(request, b_id):
    bid = ConstructionBid.objects.get(pk=b_id)

    if request.method == "POST":
        bids = AcceptConstBid()
        bids.bid_ID = bid
        bids.date = datetime.datetime.now().date()
        bids.save()
        bids = ConstructionTender.objects.filter(pk=bid.Tender_ID_id).update(tender_award='Yes')
        return redirect('tender_history')


@login_required
def bid_info(request, bid):
    bids = AcceptConstBid.objects.filter(bid_ID__user=bid)
    fbids = AcceptFurnBid.objects.filter(bid_ID__user=bid)
    dbids = AcceptBid.objects.filter(bid_ID__user=bid)
    name = Profile.objects.get(user=bid)

    fcount = fbids.count()
    fcount += dbids.count()
    fcount += bids.count()
    context = {
        'bid': bids,
        'fbid': fbids,
        'dbid': dbids,
        'fcount': fcount,
        'name': name
    }
    return render(request, "approve_bids/bidslist.html", context)


@login_required
def del_bid(request, pk):
    if request.method == 'POST':
        bid = DesktopBid.objects.get(pk=pk)
        bid.delete()
        messages.info(request, f"Bid by {bid.user.profile.company_name} for {bid.Tender_ID.Mod} rejected")

    return HttpResponse("Bid removed")


@login_required
def furn_del_bid(request, pk):
    if request.method == 'POST':
        bid = FurnitureBid.objects.get(pk=pk)
        bid.delete()
        messages.info(request, f"Bid by {bid.user.profile.company_name} for {bid.Tender_ID.Mod} rejected")
    return HttpResponse("Bid removed")


@login_required
def const_del_bid(request, pk):

    if request.method == 'POST':
        bid = ConstructionBid.objects.get(pk=pk)
        messages.info(request, f"Bid by {bid.user.profile.company_name} for {bid.Tender_ID.Mod} rejected")
        bid.delete()

    return HttpResponse("Bid removed")
