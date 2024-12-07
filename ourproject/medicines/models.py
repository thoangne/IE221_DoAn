from django.db import models
from django.urls import reverse
# Create your models here.
class Medicine(models.Model):
  medicine_id = models.CharField(max_length=5)
  name = models.CharField(max_length=20)
  catelogy_id = models.CharField(max_length=5)
  dosage_form = models.CharField(max_length=10)
  strength = models.CharField(max_length=10)
  quantity_in_stock = models.IntegerField()
  price = models.DecimalField(decimal_places=2,max_digits=10000000)
  expiry_date = models.DateField()

  def get_absolute_url(self):
    return reverse("medicines:show-detail", kwargs={"id": self.id})