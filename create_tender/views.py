from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Tender
from .forms import CreateTenderForm


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


def tenderlist(request):
    context = {
        'tenders': Tender.objects.all()
    }
    return render(request, 'create_tender/list.html', context)
