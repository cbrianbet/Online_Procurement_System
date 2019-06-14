from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import *
from .models import *
from create_tender.models import *


@login_required
def index(request, tender_id):
    tender = Desktop_Tender.objects.get(pk=tender_id)
    if request.method == 'GET':
        try:
            form = DesktopBidForm()
        except Tender.DoesNotExist:
            raise Http404("Tender does not exist")

        context = {
            'tender': tender,
            'form': form
        }
        return render(request, "create_bids/Create.html", context)

    if request.method == 'POST':
        form = DesktopBidForm(request.POST, request.FILES)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.user = request.user
            bid.Tender_ID = tender
            bid.save()
            tender.Product = form.cleaned_data.get('Product')
            tender.Memory = form.cleaned_data.get('Memory')
            tender.Graphics = form.cleaned_data.get('Graphics')
            tender.Processor = form.cleaned_data.get('Processor')
            tender.Storage = form.cleaned_data.get('Storage')
            tender.Operating_system = form.cleaned_data.get('Operating_system')
            bid.Quote_amount = form.cleaned_data.get('Quote_amount')

            messages.success(request, "Bid Posted successfully")
            return redirect('tender_feed')
        # TODO send email
        # TODO  present success
        args = {'form': form}
        return render(request, 'create_bids/Create.html', args)


@login_required
def tender_list(request):
    context = {
        'tenders': Desktop_Tender.objects.all()
    }
    return render(request, 'create_bids/Tenderlist.html', context)


@login_required
def my_bids(request):
    context = {
        'bids': Bids.objects.filter(user=request.user)
    }
    return render(request, 'create_bids/bidHistory.html', context)


@login_required
def bid_update(request, bids_id):
    try:
        bid = Bids.objects.get(pk=bids_id)
    except Bids.DoesNotExist:
        raise Http404("Tender does not exist")
    context = {
        'bid': bid
    }
    return render(request, 'create_bids/Bidupdate.html', context)


@login_required
def bid_edit(request, bids_id):
    bid = Bids.objects.get(pk=bids_id)

    if request.method == 'GET':
        try:
            form = BidForm()
        except Tender.DoesNotExist:
            raise Http404("Tender does not exist")

        context = {
            'bid': bid,
            'form': form
        }
        return render(request, "create_bids/Updatebid.html", context)

    if request.method == 'POST':
        form = BidForm(request.POST, request.FILES)
        if form.is_valid():
            bids = form.save(commit=False)
            bids.user = request.user
            bids.Tender_ID = bid.Tender_ID
            bids.id = bid
            bids.save()
            bids.Quote_amount = form.cleaned_data.get('Quote_amount')
            bids.Bid_description = form.cleaned_data.get('Bid_description')

            messages.success(request, "Bid updated successfully")
            return redirect('bid_history')
        # TODO send email
        # TODO  present success


@login_required
def del_bid(request, pk):
    if request.method == 'POST':
        bid = Bids.objects.get(pk=pk)
        bid.delete()
    return redirect('bid_history')
