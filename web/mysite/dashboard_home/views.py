from django.shortcuts import render
from django.contrib import sessions
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from dashboard_regis.models import dataCustomer
from dashboard_detail.models import customerLog
from django.shortcuts import get_object_or_404
from dashboard_home.models import contactUs


# Create your views here.

def getSessionData(request):
    sessionId = request.session.session_key
    # getId = sessionId.get_encode()
    sessionData = Session.objects.get(session_key=sessionId)
    uid = sessionData.get_decoded().get('_auth_user_id')
    return uid

def home(request):
    # return render(request, 'views/index.html')
    # paramId = getParamId(request)
    
    if request.user.is_authenticated:
        idSession = getSessionData(request)
        user = User.objects.get(id=idSession)
        data_customer = get_object_or_404(dataCustomer, email=user.email)
        paramId = data_customer.idCustomer
        logCustomer = customerLog.objects.filter(idCustomer=paramId).values()

        if logCustomer :
            logCustomer = customerLog.objects.filter(idCustomer=paramId).values().order_by('-tanggal')[0]
            context = {
                'paramId': paramId,
                'data_cust': data_customer,
                'logCustomer': logCustomer
            }
        else:
            context = {
                'paramId': paramId,
                'data_cust': data_customer,
                'logCustomer': logCustomer
            }

        return render(request, 
            'home_page/index_login.html', context)
    else:
        return render(request, 'home_page/index.html')    

def home1(request):
    # if sessions.backends.signed_cookies
    s = SessionStore()
    if request.user.is_authenticated:
        return render(request, 'home_page/index_login.html')
    else:
        return render(request, 'home_page/index.html')        

def getContactUs(request):

    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']

    message_contactUs = contactUs(
        name_contactUs= name,
        email_contactUs= email,
        subject_contactUs= subject,
        message_contactUs= message
    )

    message_contactUs.save()
    return HttpResponseRedirect(redirect_to='/')

def home_login(request):
    return render(request, 'views/index_login.html')

def test(request):
    return render(request, 'views/index_1.html')