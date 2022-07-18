from django.shortcuts import render

# Create your views here.

def billpay(request, paramId):
    return render(request, 'billpay_page/billpay_dashboard.html')