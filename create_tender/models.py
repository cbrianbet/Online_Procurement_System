from django.db import models
from core.models import Profile


# Create your models here.
class CreateTender(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    tender_title = models.CharField(max_length=64)
    tender_desc = models.CharField(max_length=500)
    date_created = models.DateField(auto_now=True)
    is_active = models.CharField(max_length=10, default=None)
    tender_value = models.PositiveIntegerField()
    tender_duration = models.PositiveIntegerField(default=10)

    def __str__(self):
        return 'tender_title'

    class Meta:
        ordering = ['-date_created']
