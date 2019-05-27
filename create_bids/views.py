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
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.user = request.user
            bid.Tender_ID = Tender.objects.get()
            bid.save()
            bid.Quote_amount = form.cleaned_data.get('Quote_amount')
            bid.Bid_description = form.cleaned_data.get('Bid_description')
            bid.Bid_documents_url = form.cleaned_data.get('Bid_documents_url')

            messages.success(request, "Tender Posted successfully")
            form = BidForm()
            return redirect('bid_feed')
        # TODO send email
        # TODO  present success
        # TODO add documents

        context = {
            'form': form
        }

        return render(request, 'create_bids/Create.html', context)


@login_required
def bidlist(request):
    context = {
        'tenders': Tender.objects.all()
    }
    return render(request, 'create_bids/Bidlist.html', context)


@login_required
def my_bids(request):
    context = {
        'bids': Bids.objects.filter(user=request.user)
    }
    return render(request, 'create_bids/bidHistory.html', context)
