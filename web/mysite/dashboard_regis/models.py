from django.db import models

# Create your models here.
class dataCustomer(models.Model):
    idCustomer = models.CharField(max_length=50, null=False, primary_key=True)
    name = models.CharField(max_length=20, null=False)
    address = models.TextField(max_length=100)
    phoneNumber = models.BigIntegerField(null=False)
    email = models.EmailField(max_length=20, null=False)
    password = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.idCustomer