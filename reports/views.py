from django.views.generic import View
from django.utils import timezone
from approve_bids.models import *
from .to_pdf import Render


class GeneratePdf(View):

    def get(self, request, tender_id):
        sales = AcceptBid.objects.get(bid_ID__Tender_ID_id=tender_id)
        number = sales.bid_ID.Quote_amount * sales.bid_ID.Tender_ID.Quantity
        today = timezone.now()
        bidc = DesktopBid.objects.filter(Tender_ID_id=tender_id).count()
        params = {
            'bidc': bidc,
            'today': today,
            'sales': sales,
            'request': request,
            'num': number
        }
        return Render.render('reports/report.html', params)


class GenerateFurnPdf(View):

    def get(self, request, tender_id):
        sales = AcceptFurnBid.objects.get(bid_ID__Tender_ID_id=tender_id)
        number = sales.bid_ID.Quote_amount * sales.bid_ID.Tender_ID.Quantity
        today = timezone.now()
        bidc = FurnitureBid.objects.filter(Tender_ID_id=tender_id).count()
        params = {
            'bidc': bidc,
            'today': today,
            'sales': sales,
            'request': request,
            'num': number
        }
        return Render.render('reports/freport.html', params)


class GenerateConstPdf(View):

    def get(self, request, tender_id):
        sales = AcceptConstBid.objects.get(bid_ID__Tender_ID_id=tender_id)
        number = sales.bid_ID.Quote_amount * sales.bid_ID.Tender_ID.Quantity
        today = timezone.now()
        bidc = ConstructionBid.objects.filter(Tender_ID_id=tender_id).count()
        params = {
            'bidc': bidc,
            'today': today,
            'sales': sales,
            'request': request,
            'num': number
        }
        return Render.render('reports/creport.html', params)
