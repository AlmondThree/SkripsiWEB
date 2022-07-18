from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django import template
from dashboard_regis.models import dataCustomer
from dashboard_detail.models import customerLog
from django.shortcuts import get_object_or_404

register = template.Library()

@login_required(redirect_field_name='next', login_url='/login/')
def detail(request, paramId):
    idSession = getSessionData(request)
    user = User.objects.get(id=idSession)
    data_customer = get_object_or_404(dataCustomer, email=user.email)
    # paramId = data_customer.idCustomer
    
    id_customer = data_customer.idCustomer

    logCustomer = customerLog.objects.filter(idCustomer=id_customer).values().order_by('-tanggal')[0]

    context = {'data': user,
         'id': user.id,
         'data_cust': data_customer,
         'logCustomer': logCustomer}

    return render(request,
        'detail_page/detail_dashboard.html',
        context)

def description(request, paramPage):
    
    return render(request, 'detail_page/detail_description.html')

def getSessionData(request):
    sessionId = request.session.session_key
    # getId = sessionId.get_encode()
    sessionData = Session.objects.get(session_key=sessionId)
    uid = sessionData.get_decoded().get('_auth_user_id')
    return uid