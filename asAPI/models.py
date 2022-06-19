from django.db import models

# Create your models here.
    
class ASInformation(models.Model):
    id = models.AutoField(default=0, primary_key=True)
    range_start = models.TextField()
    range_end = models.TextField(default='0.0.0.0')
    as_number = models.TextField(blank=0)
    country_code = models.CharField(max_length=2, blank=True, default=None)
    as_description = models.TextField()

