from django.db import models
from create_tender.models import CreateTender
from core.models import Profile


class Bids(models.Model):
    Tender_ID = models.ForeignKey(CreateTender, on_delete=models.CASCADE)
    User_ID = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Quote_amount = models.IntegerField()
    Bid_description = models.TextField(max_length=500)
    Bid_documents_url = models.FileField()
    Bid_created_date = models.DateField(auto_now_add=True)
