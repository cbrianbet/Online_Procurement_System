from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone

from .forms import *
from .models import *
from reports.to_pdf import *
from create_tender.models import *
from approve_bids.models import *


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
            bid.Product = form.cleaned_data.get('Product')
            bid.Memory = form.cleaned_data.get('Memory')
            bid.Graphics = form.cleaned_data.get('Graphics')
            bid.Processor = form.cleaned_data.get('Processor')
            bid.Storage = form.cleaned_data.get('Storage')
            bid.Operating_system = form.cleaned_data.get('Operating_system')
            bid.Quote_amount = form.cleaned_data.get('Quote_amount')

            messages.success(request, "Bid Posted successfully")
            return redirect('tender_feed')
        # TODO send email
        args = {'form': form}
        return render(request, 'create_bids/Create.html', args)


@login_required
def furn_bid(request, tender_id):
    tender = FurnitureTender.objects.get(pk=tender_id)
    if request.method == 'GET':
        try:
            form = FurnitureBidForm()
        except Tender.DoesNotExist:
            raise Http404("Tender does not exist")

        context = {
            'tender': tender,
            'form': form
        }
        return render(request, "create_bids/FurnCreate.html", context)

    if request.method == 'POST':
        form = FurnitureBidForm(request.POST, request.FILES)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.user = request.user
            bid.Tender_ID = tender
            bid.save()
            bid.Color = form.cleaned_data.get('Color')
            bid.Product = form.cleaned_data.get('Product')
            bid.Material = form.cleaned_data.get('Material')
            bid.Dimensions = form.cleaned_data.get('Dimensions')
            bid.Quote_amount = form.cleaned_data.get('Quote_amount')

            messages.success(request, "Bid Posted successfully")
            return redirect('tender_feed')
        # TODO send email
        args = {'form': form}
        return render(request, 'create_bids/FurnCreate.html', args)


@login_required
def const_bid(request, tender_id):
    tender = ConstructionTender.objects.get(pk=tender_id)
    if request.method == 'GET':
        try:
            form = ConstructionBidForm()
        except Tender.DoesNotExist:
            raise Http404("Tender does not exist")

        context = {
            'tender': tender,
            'form': form
        }
        return render(request, "create_bids/ConstCreate.html", context)

    if request.method == 'POST':
        form = ConstructionBidForm(request.POST, request.FILES)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.user = request.user
            bid.Tender_ID = tender
            bid.save()
            bid.Net_power = form.cleaned_data.get('Net_power')
            bid.Certification = form.cleaned_data.get('Certification')
            bid.Mod = form.cleaned_data.get('Mod')
            bid.Operating_weight = form.cleaned_data.get('Operating_weight')
            bid.Electric = form.cleaned_data.get('Electric')
            bid.Engine = form.cleaned_data.get('Engine')
            bid.Quote_amount = form.cleaned_data.get('Quote_amount')

            messages.success(request, "Bid Posted successfully")
            return redirect('tender_feed')
        # TODO send email
        args = {'form': form}
        return render(request, 'create_bids/ConstCreate.html', args)


@login_required
def tender_list(request):
    context = {
        'tenders': Desktop_Tender.objects.filter(is_active__exact='Yes')
    }
    return render(request, 'create_bids/Tenderlist.html', context)


@login_required
def tender_list_f(request):
    context = {
        'furnTender': FurnitureTender.objects.exclude(is_active__exact='Yes')
    }
    return render(request, 'create_bids/Tenderlistf.html', context)


@login_required
def tender_list_c(request):
    context = {
        'constTender': ConstructionTender.objects.filter(is_active__exact='Yes')
    }
    return render(request, 'create_bids/TenderlistC.html', context)


@login_required
def my_bids(request):
    context = {
        'deskbid': DesktopBid.objects.filter(user=request.user),
        'bids': Bids.objects.filter(user=request.user)
    }
    return render(request, 'create_bids/bidHistory.html', context)


@login_required
def my_bids_c(request):
    context = {
        'constbid': ConstructionBid.objects.filter(user=request.user),
        'bids': Bids.objects.filter(user=request.user)
    }
    return render(request, 'create_bids/bidHistoryC.html', context)


@login_required
def my_bids_f(request):
    context = {
        'furnbid': FurnitureBid.objects.filter(user=request.user),
        'bids': Bids.objects.filter(user=request.user)
    }
    return render(request, 'create_bids/bidHistoryF.html', context)


@login_required
def bid_update(request, bids_id):
    try:
        bid = DesktopBid.objects.get(pk=bids_id)
    except Bids.DoesNotExist:
        raise Http404("Tender does not exist")
    context = {
        'bid': bid
    }
    return render(request, 'create_bids/Bidupdate.html', context)


@login_required
def const_bid_update(request, bids_id):
    try:
        bid = ConstructionBid.objects.get(pk=bids_id)
    except Bids.DoesNotExist:
        raise Http404("Tender does not exist")
    context = {
        'bid': bid
    }
    return render(request, 'create_bids/ConstBidupdate.html', context)


@login_required
def furn_bid_update(request, bids_id):
    try:
        bid = FurnitureBid.objects.get(pk=bids_id)
    except Bids.DoesNotExist:
        raise Http404("Tender does not exist")
    context = {
        'bid': bid
    }
    return render(request, 'create_bids/FurnBidupdate.html', context)


@login_required
def bid_edit(request, bids_id):
    bid = DesktopBid.objects.get(pk=bids_id)

    if request.method == 'GET':
        try:
            form = DesktopBidForm()
        except Tender.DoesNotExist:
            raise Http404("Tender does not exist")

        context = {
            'bid': bid,
            'form': form
        }
        return render(request, "create_bids/Updatebid.html", context)

    if request.method == 'POST':
        form = DesktopBidForm(request.POST, request.FILES)
        if form.is_valid():
            bids = form.save(commit=False)
            bids.user = request.user
            bids.Tender_ID = bid.Tender_ID
            bids.id = bid.id
            bids.save()
            bids.Product = form.cleaned_data.get('Product')
            bids.Memory = form.cleaned_data.get('Memory')
            bids.Graphics = form.cleaned_data.get('Graphics')
            bids.Processor = form.cleaned_data.get('Processor')
            bids.Storage = form.cleaned_data.get('Storage')
            bids.Operating_system = form.cleaned_data.get('Operating_system')
            bids.Quote_amount = form.cleaned_data.get('Quote_amount')

            messages.success(request, "Bid updated successfully")
            return redirect('bid_history')
        # TODO send email


@login_required
def furn_bid_edit(request, bids_id):
    bid = FurnitureBid.objects.get(pk=bids_id)

    if request.method == 'GET':
        try:
            form = FurnitureBidForm()
        except Tender.DoesNotExist:
            raise Http404("Tender does not exist")

        context = {
            'bid': bid,
            'form': form
        }
        return render(request, "create_bids/Updatebid.html", context)

    if request.method == 'POST':
        form = FurnitureBidForm(request.POST, request.FILES)
        if form.is_valid():
            bids = form.save(commit=False)
            bids.user = request.user
            bids.Tender_ID = bid.Tender_ID
            bids.id = bid.id
            bids.save()
            bids.Color = form.cleaned_data.get('Color')
            bids.Product = form.cleaned_data.get('Product')
            bids.Material = form.cleaned_data.get('Material')
            bids.Dimensions = form.cleaned_data.get('Dimensions')
            bids.Quote_amount = form.cleaned_data.get('Quote_amount')

            messages.success(request, "Bid updated successfully")
            return redirect('bid_history')
        # TODO send email


@login_required
def const_bid_edit(request, bids_id):
    bid = ConstructionBid.objects.get(pk=bids_id)

    if request.method == 'GET':
        try:
            form = ConstructionBidForm()
        except Tender.DoesNotExist:
            raise Http404("Tender does not exist")

        context = {
            'bid': bid,
            'form': form
        }
        return render(request, "create_bids/Updatebid.html", context)

    if request.method == 'POST':
        form = ConstructionBidForm(request.POST, request.FILES)
        if form.is_valid():
            bids = form.save(commit=False)
            bids.user = request.user
            bids.Tender_ID = bid.Tender_ID
            bids.id = bid.id
            bids.save()
            bids.Net_power = form.cleaned_data.get('Net_power')
            bids.Certification = form.cleaned_data.get('Certification')
            bids.Mod = form.cleaned_data.get('Mod')
            bids.Operating_weight = form.cleaned_data.get('Operating_weight')
            bids.Electric = form.cleaned_data.get('Electric')
            bids.Engine = form.cleaned_data.get('Engine')
            bids.Quote_amount = form.cleaned_data.get('Quote_amount')

            messages.success(request, "Bid updated successfully")
            return redirect('bid_history')
        # TODO send email


@login_required
def del_bid(request, pk):
    if request.method == 'POST':
        bid = DesktopBid.objects.get(pk=pk)
        bid.delete()
    return redirect('bid_history')


@login_required
def furn_del_bid(request, pk):
    if request.method == 'POST':
        bid = FurnitureBid.objects.get(pk=pk)
        bid.delete()
    return redirect('bid_history')


@login_required
def const_del_bid(request, pk):
    if request.method == 'POST':
        bid = ConstructionBid.objects.get(pk=pk)
        bid.delete()
    return redirect('bid_history')


def aw_rep(request):
    const = AcceptConstBid.objects.filter(bid_ID__user=request.user)
    furn = AcceptFurnBid.objects.filter(bid_ID__user=request.user)
    desk = AcceptBid.objects.filter(bid_ID__user=request.user)
    number = const.count() + furn.count() + desk.count()
    today = timezone.now()

    params = {
        'today': today,
        'sales': const,
        'furn': furn,
        'desk': desk,
        'request': request,
        'num': number
    }
    return Render.render('create_bids/report.html', params)
