from django.db import models
from core.models import Profile


# Create your models here.
class Tender(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    tender_title = models.CharField(max_length=64)
    tender_desc = models.CharField(max_length=500)
    date_created = models.DateField(auto_now=True)
    is_active = models.CharField(max_length=10, default=None)
    tender_value = models.PositiveIntegerField(null=True)
    tender_duration = models.PositiveIntegerField(default=10)
    tender_award = models.CharField(max_length=10, default="No")

    def __str__(self):
        return f"{self.tender_title}"

    class Meta:
        ordering = ['-date_created']
