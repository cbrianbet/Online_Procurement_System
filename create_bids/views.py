from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import BidForm
from .models import Bids
from create_tender.models import Tender


@login_required
def index(request, tender_id):
    tender = Tender.objects.get(pk=tender_id)
    if request.method == 'GET':
        try:
            form = BidForm()
        except Tender.DoesNotExist:
            raise Http404("Tender does not exist")

        context = {
            'tender': tender,
            'form': form
        }
        return render(request, "create_bids/Create.html", context)

    if request.method == 'POST':
        form = BidForm(request.POST, request.FILES)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.user = request.user
            bid.Tender_ID = tender
            bid.save()
            bid.Quote_amount = form.cleaned_data.get('Quote_amount')
            bid.Bid_description = form.cleaned_data.get('Bid_description')

            messages.success(request, "Bid Posted successfully")
            form = BidForm()
            return redirect('tender_feed')
        # TODO send email
        # TODO  present success

        context = {
            'form': form
        }

        return render(request, 'create_bids/Create.html', context)


@login_required
def tender_list(request):
    context = {
        'tenders': Tender.objects.filter(is_active__exact="Yes")
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
def del_bid(request, pk):
    if request.method == 'POST':
        bid = Bids.objects.get(pk=pk)
        bid.delete()
    return redirect('bid_history')
