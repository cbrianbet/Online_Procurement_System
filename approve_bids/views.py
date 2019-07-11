import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Min
from django.core.mail import send_mail

from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from create_bids.models import FurnitureBid, DesktopBid, ConstructionBid
from create_tender.models import *


@login_required
def bid_for_tender_list(request, bid_id):
    bids = DesktopBid.objects.filter(Tender_ID_id=bid_id, bid_award='null')
    tender = Desktop_Tender.objects.get(pk=bid_id)
    context = {
        'bids': bids,
        'tender': tender
    }
    return render(request, 'approve_bids/tenderBid.html', context)


@login_required
def bid_furn_tender_list(request, bid_id):
    bids = FurnitureBid.objects.filter(Tender_ID_id=bid_id, bid_award='null')
    tender = FurnitureTender.objects.get(pk=bid_id)
    context = {
        'fbids': bids,
        'tender': tender
    }
    return render(request, 'approve_bids/furnTenderBid.html', context)


@login_required
def bid_const_tender_list(request, tender_id):
    bids = ConstructionBid.objects.filter(Tender_ID_id=tender_id, bid_award='null')
    tender = ConstructionTender.objects.get(pk=tender_id)
    context = {
        'cbids': bids,
        'tender': tender
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
        DesktopBid.objects.filter(pk=b_id).update(bid_award='Yes')
        Desktop_Tender.objects.filter(pk=bid.Tender_ID.id).update(tender_award='Yes')
        Desktop_Tender.objects.filter(pk=bid.Tender_ID.id).update(is_active='No')
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
        FurnitureBid.objects.filter(pk=b_id).update(bid_award='Yes')
        FurnitureTender.objects.filter(pk=bid.Tender_ID_id.id).update(tender_award='Yes')
        FurnitureTender.objects.filter(pk=bid.Tender_ID_id.id).update(is_active='No')
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
        ConstructionBid.objects.filter(pk=b_id).update(bid_award='Yes')
        ConstructionTender.objects.filter(pk=bid.Tender_ID.id).update(tender_award='Yes')
        ConstructionTender.objects.filter(pk=bid.Tender_ID.id).update(is_active='No')
        messages.success(request, f"Bid by {bid.user.profile.company_name} for {bid.Tender_ID.Product} accepted")
        return redirect('tender_history')


@login_required
def bid_info(request, bid):
    bids = AcceptConstBid.objects.filter(bid_ID__user_id=bid)
    fbids = AcceptFurnBid.objects.filter(bid_ID__user_id=bid)
    dbids = AcceptBid.objects.filter(bid_ID__user_id=bid)
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
def desk_bid_info(request, bid):
    bids = AcceptBid.objects.filter(bid_ID__user_id=bid)
    fbids = AcceptFurnBid.objects.filter(bid_ID__user_id=bid)
    dbids = AcceptConstBid.objects.filter(bid_ID__user_id=bid)
    name = User.objects.get(pk=bid)

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
def furn_bid_info(request, bid):
    bids = AcceptFurnBid.objects.filter(bid_ID__user=bid)
    fbids = AcceptConstBid.objects.filter(bid_ID__user=bid)
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
        DesktopBid.objects.filter(pk=pk).update(bid_award='No')
        messages.info(request, f"Bid by {bid.user.profile.company_name} for {bid.Tender_ID.Product} rejected")

    return redirect("tender_history")


@login_required
def furn_del_bid(request, pk):
    if request.method == 'POST':
        bid = FurnitureBid.objects.get(pk=pk)
        FurnitureTender.objects.get(pk=pk).update(bid_award='No')
        messages.info(request, f"Bid by {bid.user.profile.company_name} for {bid.Tender_ID.Product} rejected")
    return redirect('tender_history')


@login_required
def const_del_bid(request, pk):

    if request.method == 'POST':
        bid = ConstructionBid.objects.get(pk=pk)
        ConstructionBid.objects.get(pk=pk).update(bid_award='No')
        messages.info(request, f"Bid by {bid.user.profile.company_name} for {bid.Tender_ID.Mod} rejected")
    return redirect('tender_history')


@login_required
def furn_view_bid(request, bid):
    context = {
        'atend': FurnitureBid.objects.get(pk=bid)
    }
    return render(request, 'approve_bids/view.html', context)


@login_required
def view_bid(request, bid):
    context = {
        'atend': DesktopBid.objects.get(pk=bid)
    }
    return render(request, 'approve_bids/deskView.html', context)


@login_required
def const_view_bid(request, bid):
    context = {
        'atend': ConstructionBid.objects.get(pk=bid)
    }
    return render(request, 'approve_bids/constView.html', context)

#
# @login_required
# def auto_award(request, tender_id):
#     bid = DesktopBid.objects.filter(Tender_ID_id=tender_id).aggregate(Min('Quote_amount'))
#     bid.update(bid_award='Yes')
#     if request.method == "POST":
#         bids = AcceptBid()
#         bids.bid_ID. = bid
#         bids.date = datetime.datetime.now().date()
#         bids.save()
#         bids = Desktop_Tender.objects.filter(pk=bid.Tender_ID_id).update(tender_award='Yes')
#
#         messages.success(request, f"Bid by {bid.user.profile.company_name} for {bid.Tender_ID.Product} accepted")
#     return redirect('tender_history')
#
#
# @login_required
# def const_auto_award(request, tender_id):
#     bid = ConstructionBid.objects.filter(Tender_ID_id=tender_id).aggregate(Min('Quote_amount'))
#     bid.update(bid_award='Yes')
#     if request.method == "POST":
#         bids = AcceptConstBid()
#         bids.bid_ID = bid
#         bids.date = datetime.datetime.now().date()
#         bids.save()
#         bids = ConstructionTender.objects.filter(pk=bid.Tender_ID_id).update(tender_award='Yes')
#
#         messages.success(request, f"Bid by {bid.user.profile.company_name} for {bid.Tender_ID.Product} accepted")
#     return redirect('tender_history')
