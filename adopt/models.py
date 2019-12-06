from django.db import models
class show(models.Model):
    CHOICES = (('AM', 'AM'),('PM', 'PM'))
    Longitude = models.FloatField()
    Latitude = models.FloatField()
    Unique_squirrel_id = models.CharField(max_length=30,primary_key=True)
    Shift = models.CharField(max_length=2, choices=CHOICES)
    Date = models.DateField()
    Age = models.CharField(max_length=20, null=True, blank=True)
    Primary_fur_color = models.CharField(max_length=30, null=True, blank=True)
    Location = models.CharField(max_length=50, null=True, blank=True)
    Specific_location = models.CharField(max_length=50, null=True, blank=True)
    Running = models.BooleanField()
    Chasing = models.BooleanField()
    Climbing = models.BooleanField()
    Eating = models.BooleanField()
    Foraging = models.BooleanField()
    Other_activities = models.CharField(max_length=80, null=True, blank=True)
    Kuks = models.BooleanField()
    Quaas = models.BooleanField()
    Moans = models.BooleanField()
    Tail_flags = models.BooleanField()
    Tail_twitches = models.BooleanField()
    Approaches = models.BooleanField()
    Indifferent = models.BooleanField()
    Runs_from = models.BooleanField()
# Create your models here.
