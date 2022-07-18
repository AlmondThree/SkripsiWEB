from django.db import models
from dashboard_regis.models import dataCustomer
from dashboard_detail.models import customerLog, History

# Create your models here.

class Billpay(models.Model):
    idCustomer = models.ForeignKey(dataCustomer, on_delete=models.CASCADE, primary_key=True)
    # month = models.ForeignKey(customerLog, to_field= "tanggal", on_delete=models.CASCADE)
    month = models.ManyToManyField(
        to=History,
        db_column= 'month',
    )
    # montlyUsage = models.OneToOneField(customerLog, to_field="usageMonthly" ,on_delete=models.CASCADE)
    billpay = models.IntegerField()
    billpayStatus = models.CharField(max_length=10)
    # status = models.OneToOneField(
    #     customerLog,
    #     on_delete=models.CASCADE)