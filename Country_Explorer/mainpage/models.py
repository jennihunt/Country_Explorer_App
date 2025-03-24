from django.db import models
from djmoney.models.fields import MoneyField


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capital = models.CharField(max_length=255, blank=True, null=True)
    currencies=MoneyField(max_digits=10, decimal_places=2, default_currency='USD', default=0)
    population = models.BigIntegerField(blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    subregion = models.CharField(max_length=255, blank=True, null=True)
    flag_url = models.URLField(blank=True, null=True)
    languages=models.CharField(max_length=255, blank=True, null=True)
    continents=models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name