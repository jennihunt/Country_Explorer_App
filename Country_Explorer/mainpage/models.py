from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=500, unique=True)
    capital = models.CharField(max_length=500, blank=True, null=True)
   
    currencies = models.JSONField(default=dict, null=True, blank=True) 
    population = models.BigIntegerField(blank=True, null=True)
    region = models.CharField(max_length=500, blank=True, null=True)
    subregion = models.CharField(max_length=500, blank=True, null=True)
    flag_url = models.URLField(blank=True, null=True)
    
    languages=models.JSONField(null=True, blank=True)
    continents=models.CharField(max_length=500, blank=True, null=True)
    last_updated=models.DateTimeField(auto_now=True)  # Ensure this field is present


   
    def __str__(self):
        return self.name