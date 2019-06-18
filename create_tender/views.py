from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from create_bids.models import Bids
from .models import *
from .forms import *
from approve_bids.models import *


@login_required
def index(request):
    if request.method == 'GET':
        form = DesktopTenderForm()
        return render(request, "create_tender/Create.html", {'form': form})

    if request.method == 'POST':
        form = DesktopTenderForm(request.POST)
        if form.is_valid():
            tender = form.save(commit=False)
            tender.user = request.user
            tender.save()
            tender.Product = form.cleaned_data.get('Product')
            tender.Memory = form.cleaned_data.get('Memory')
            tender.Graphics = form.cleaned_data.get('Graphics')
            tender.Processor = form.cleaned_data.get('Processor')
            tender.Storage = form.cleaned_data.get('Storage')
            tender.Operating_system = form.cleaned_data.get('Operating_system')
            tender.Quantity = form.cleaned_data.get('Quantity')
            messages.success(request, "Tender Posted successfully")
            return redirect('desktp_tender')
        # TODO send email
        # TODO  present success
        args = {'form': form}
        return render(request, 'create_tender/Create.html', args)


@login_required
def const_tender(request):
    if request.method == 'GET':
        form = ConstTenderForm()
        return render(request, "create_tender/Create.html", {'form': form})

    if request.method == 'POST':
        form = ConstTenderForm(request.POST)
        if form.is_valid():
            tender = form.save(commit=False)
            tender.user = request.user
            tender.save()
            tender.Mod = form.cleaned_data.get('Mod')
            tender.Net_power = form.cleaned_data.get('Net_power')
            tender.Electric = form.cleaned_data.get('Electric')
            tender.Operating_weight = form.cleaned_data.get('Operating_weight')
            tender.Certification = form.cleaned_data.get('Certification')
            tender.Engine = form.cleaned_data.get('Engine')
            tender.Quantity = form.cleaned_data.get('Quantity')
            messages.success(request, "Tender Posted successfully")
            return redirect('constTender')
        # TODO send email
        # TODO  present success
        args = {'form': form}
        return render(request, 'create_tender/Create.html', args)


@login_required
def furn_tender(request):
    if request.method == 'GET':
        form = FurnitureTenderForm()
        return render(request, "create_tender/Create.html", {'form': form})

    if request.method == 'POST':
        form = FurnitureTenderForm(request.POST)
        if form.is_valid():
            tender = form.save(commit=False)
            tender.user = request.user
            tender.save()
            tender.Product = form.cleaned_data.get('Product')
            tender.Dimensions = form.cleaned_data.get('Dimensions')
            tender.Material = form.cleaned_data.get('Material')
            tender.Color = form.cleaned_data.get('Color')
            tender.Quantity = form.cleaned_data.get('Quantity')
            messages.success(request, "Tender Posted successfully")
            return redirect('furnitureTender')
        # TODO send email
        # TODO  present success
        args = {'form': form}
        return render(request, 'create_tender/Create.html', args)


@login_required
def my_tenders(request):
    awarded_tender = AcceptBid.objects.filter(bid_ID__Tender_ID__user=request.user)
    awarded_furn_tender = AcceptFurnBid.objects.filter(bid_ID__Tender_ID__user=request.user)
    awarded_const_tender = AcceptConstBid.objects.filter(bid_ID__Tender_ID__user=request.user)
    my_tender = Desktop_Tender.objects.filter(user=request.user, tender_award__exact="No")
    my_const_tender = ConstructionTender.objects.filter(user=request.user, tender_award__exact="No")
    my_furn_tender = FurnitureTender.objects.filter(user=request.user, tender_award__exact="No")
    context = {
        "acc_bids": awarded_tender,
        'acc_furn': awarded_furn_tender,
        'acc_const': awarded_const_tender,
        'my_tender': my_tender,
        'my_furn': my_const_tender,
        'my_const': my_furn_tender
    }
    return render(request, 'create_tender/tenderHistory.html', context)


@login_required
def tender_type(request):
    return render(request, "create_tender/tenderType.html")


@login_required
def del_tender(request, pk):
    if request.method == 'POST':
        tender = Desktop_Tender.objects.get(pk=pk)
        messages.error(request, f"{tender.tender_title} deleted")
        tender.delete()
    return redirect('tender_history')


@login_required
def acc_list(request, bid_id):
    context = {
        "bid": AcceptBid.objects.filter(id=bid_id)
    }
    return render(request, "create_tender/acc_bid.html", context)
