# Create your models here.
from django.db import models
class Product(models.Model):
   p_id=models.AutoField(primary_key=True)
   p_name=models.CharField(max_length=200)
   p_company=models.CharField(max_length=200)
   p_price =models.FloatField()
