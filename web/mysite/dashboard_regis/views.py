from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from dashboard_regis.models import dataCustomer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
import string
import random

# Create your views here.
def home(request):
    return render(request, 'regis_page/regis_dashboard.html')

def getID(length):
    letters = string.ascii_letters
    result = ''.join(random.choice(letters) for i in range(length))
    return result

def createUser(usrname, pw, email, nama):
    password_hash = make_password(pw)
    user = User.objects.create(username=usrname, password=password_hash, email=email, first_name=nama)
    user.save()

def customerRegis(request):
    idCustomer = getID(7)
    nama = request.POST['nama']
    alamat = request.POST['alamat']
    nomorHP = request.POST['nomorHP']
    email = request.POST['email']
    pw = request.POST['pw']

    dataCustomer_regis = dataCustomer(
        idCustomer=idCustomer, 
        name= nama, 
        address= alamat, 
        phoneNumber= nomorHP, 
        email= email, 
        password= make_password(pw)
    )

    if User.objects.exclude().filter(username=email).exists():
        return render(request,
            'regis_page/regis_dashboard.html',
            {'isValid': True,
             'logError': 'Alamat email sudah digunakan'
            })
    else:
        dataCustomer_regis.save()
        createUser(email, pw, email, nama)
        return HttpResponseRedirect(reverse('index'))