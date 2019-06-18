from django.db import models
from create_bids.models import DesktopBid, FurnitureBid, ConstructionBid


class AcceptBid(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    bid_ID = models.OneToOneField(DesktopBid, on_delete=models.CASCADE)


class AcceptConstBid(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    bid_ID = models.OneToOneField(ConstructionBid, on_delete=models.CASCADE)


class AcceptFurnBid(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    bid_ID = models.OneToOneField(FurnitureBid, on_delete=models.CASCADE)
