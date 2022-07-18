from django.db import models

# Create your models here.
class contactUs(models.Model):
    name_contactUs = models.CharField(max_length=50)
    email_contactUs = models.EmailField()
    subject_contactUs = models.CharField(max_length=100)
    message_contactUs = models.CharField(max_length=1000)