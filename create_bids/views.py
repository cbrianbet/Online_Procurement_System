from django.shortcuts import render
from .forms import BidForm


def index(request):
    if request.method == 'GET':
        form = BidForm()
        return render(request, "create_bids/Create.html", {'form': form})

    if request.method == 'POST':
        # TODO send email
        # TODO write to DB
        # TODO  present success
        return render(request, 'create_bids/Create.html')
