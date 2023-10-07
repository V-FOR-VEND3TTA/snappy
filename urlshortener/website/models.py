from django.db import models

# Create your models here.
class Url(models.Model):
    link = models.CharField(max_length=10000) # the link we give to the page form
    uuid = models.CharField(max_length=10) # the specific id we give to the link above

