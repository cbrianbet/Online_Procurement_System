from django.db import models
from create_bids.models import Bids


class AcceptBid(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    bid_ID = models.OneToOneField(Bids, on_delete=models.CASCADE)
