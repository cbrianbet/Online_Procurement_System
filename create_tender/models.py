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


class Desktop_Tender(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    Product = models.CharField(max_length=120)
    Processor = models.CharField(max_length=120)
    Operating_system = models.CharField(max_length=80)
    Memory = models.CharField(max_length=100)
    Storage = models.CharField(max_length=100)
    Graphics = models.CharField(max_length=100)
    tender_award = models.CharField(max_length=10, default="No")
    date_created = models.DateField(auto_now=True)
    Quantity = models.PositiveIntegerField()
    is_active = models.CharField(max_length=10, default='Yes')

    def __str__(self):
        return f"{self.Product} by {self.user.profile.company_name}"

    class Meta:
        ordering = ['-date_created']


class ConstructionTender(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    Mod = models.CharField(max_length=80)
    Net_power = models.CharField(max_length=80)
    Electric = models.CharField(max_length=80)
    Engine = models.CharField(max_length=80, default="No")
    Operating_weight = models.CharField(max_length=80)
    Certification = models.CharField(max_length=80)
    Quantity = models.PositiveIntegerField()
    tender_award = models.CharField(max_length=10, default="No")
    date_created = models.DateField(auto_now=True)
    is_active = models.CharField(max_length=10, default='Yes')

    def __str__(self):
        return f"{self.Mod} by {self.user.profile.company_name}"

    class Meta:
        ordering = ['-date_created']


class FurnitureTender(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    Product = models.CharField(max_length=100)
    Dimensions = models.CharField(max_length=80)
    Material = models.CharField(max_length=80)
    Color = models.CharField(max_length=80)
    Quantity = models.PositiveIntegerField()
    tender_award = models.CharField(max_length=10, default="No")
    is_active = models.CharField(max_length=10, default='Yes')
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.Product} by {self.user.profile.company_name}"

    class Meta:
        ordering = ['-date_created']
