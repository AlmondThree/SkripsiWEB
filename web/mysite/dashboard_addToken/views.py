from django.shortcuts import render

# Create your views here.

def addToken(request, paramId):
    return render(request, 'addToken_page/addToken_dashboard.html')