from django.db import models
from create_tender.models import Tender, Desktop_Tender
from core.models import Profile


class Bids(models.Model):
    Tender_ID = models.ForeignKey(Tender, on_delete=models.CASCADE)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, default='betts')
    Quote_amount = models.PositiveIntegerField()
    Bid_description = models.TextField(max_length=500)
    Bid_documents_url = models.FileField(upload_to='bid/documents/', null=True, blank=True)
    Bid_created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.Tender_ID.tender_title}"

    def delete(self, *args, **kwargs):
        self.Bid_documents_url.delete()
        super().delete(*args, **kwargs)

    class Meta:
        ordering = ['-Bid_created_date']


class DesktopBid(models.Model):
    Tender_ID = models.ForeignKey(Desktop_Tender, on_delete=models.CASCADE)
    Quote_amount = models.PositiveIntegerField()
    Product = models.CharField(max_length=120)
    Processor = models.CharField(max_length=120)
    Operating_system = models.CharField(max_length=80)
    Memory = models.CharField(max_length=100)
    Storage = models.CharField(max_length=100)
    Graphics = models.CharField(max_length=100)
    date_created = models.DateField(auto_now=True)
    Bid_documents_url = models.FileField(upload_to='bid/documents/', null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.Bid_documents_url.delete()
        super().delete(*args, **kwargs)

    class Meta:
        ordering = ['-date_created']
