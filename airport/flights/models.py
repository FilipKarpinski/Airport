from django.db import models

# Create your models here.

class Flight(models.Model):
    company = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    arrival_date_time = models.DateTimeField()
    start_airport = models.CharField(max_length=50)
    arrival_airport = models.CharField(max_length=50)
