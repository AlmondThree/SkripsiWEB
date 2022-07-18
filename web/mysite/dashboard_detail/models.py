from django.db import models
from dashboard_regis.models import dataCustomer

# Create your models here.
class customerLog(models.Model):
    tanggal = models.DateField(null=False)
    idCustomer = models.ForeignKey(dataCustomer, on_delete=models.CASCADE)
    limit = models.BigIntegerField()
    usage = models.BigIntegerField()
    status = models.BooleanField()

    def __date__(self):
        return self.tanggal
    
class History(models.Model):
    idCustomer = models.ForeignKey(dataCustomer, on_delete=models.CASCADE)
    # month = models.ManyToManyField(to=customerLog, db_column='tanggal')
    month = models.CharField(null=False, max_length= 10)
    limitMonthly = models.BigIntegerField()
    usageMonthly = models.BigIntegerField()