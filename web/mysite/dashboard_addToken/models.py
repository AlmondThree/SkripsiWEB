from django.db import models

# Create your models here.
class Token(models.Model):
    tokenId = models.CharField(max_length=10)
    tokenValue = models.CharField(max_length=10)
    statusToken = models.BooleanField()