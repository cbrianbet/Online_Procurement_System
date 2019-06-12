from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from create_bids.models import Bids
from .models import Tender
from .forms import CreateTenderForm
from approve_bids.models import AcceptBid


@login_required
def index(request):
    if request.method == 'GET':
        form = CreateTenderForm()
        return render(request, "create_tender/Create.html", {'form': form})

    if request.method == 'POST':
        form = CreateTenderForm(request.POST)
        if form.is_valid():
            tender = form.save(commit=False)
            tender.user = request.user
            tender.save()
            tender.tender_title = form.cleaned_data.get('tender_title')
            tender.tender_desc = form.cleaned_data.get('tender_desc')
            tender.tender_duration = form.cleaned_data.get('tender_duration')
            tender.tender_value = form.cleaned_data.get('tender_value')
            tender.is_active = form.cleaned_data.get('is_active')
            messages.success(request, "Tender Posted successfully")
            form = CreateTenderForm()
            return redirect('create_tender')
        # TODO send email
        # TODO  present success
        args = {'form': form}
        return render(request, 'create_tender/Create.html', args)


@login_required
def tenderlist(request):
    context = {
        'tenders': Tender.objects.all()
    }
    return render(request, 'create_tender/list.html', context)


@login_required
def my_tenders(request):

    awarded_tender = AcceptBid.objects.filter(bid_ID__Tender_ID__user=request.user)
    my_tender = Tender.objects.filter(user=request.user, tender_award__exact="No")

    context = {
        "acc_bids": awarded_tender,
        'my_tender': my_tender
    }
    return render(request, 'create_tender/tenderHistory.html', context)


@login_required
def del_tender(request, pk):
    if request.method == 'POST':
        tender = Tender.objects.get(pk=pk)
        messages.error(request, f"{tender.tender_title} deleted")
        tender.delete()
    return redirect('tender_history')
