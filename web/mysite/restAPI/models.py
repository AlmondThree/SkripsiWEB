from django.db import models

# Create your models here.
class customerId(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_join = models.DateField(null=True)
    customer_description = models.TextField(max_length=100)

    def __str__(self):
        return self.customer_name

class Data(models.Model):
    nama_pelanggan = models.ForeignKey(customerId, on_delete=models.CASCADE)
    tanggal = models.DateField(null=True)
    tekanan = models.IntegerField()
    penggunaan = models.IntegerField()
    limit = models.IntegerField()

    def __date__(self):
        return self.tanggal

