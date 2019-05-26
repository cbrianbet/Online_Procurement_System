from django.db import models
from create_tender.models import Tender
from core.models import Profile


class Bids(models.Model):
    Tender_ID = models.ForeignKey(Tender, on_delete=models.CASCADE)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, default='betts')
    Quote_amount = models.PositiveIntegerField()
    Bid_description = models.TextField(max_length=500)
    Bid_documents_url = models.FilePathField()
    Bid_created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.Tender_ID.tender_title}"

    class Meta:
        ordering = ['-Bid_created_date']
