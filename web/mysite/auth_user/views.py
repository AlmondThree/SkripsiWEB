from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

# Create your views here.
def login(request):
    return render(request, 'auth_page/loginUser.html')

def loginUser(request):
    username = request.POST['usr_auth']
    password = request.POST['pw']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        auth_login(request, user)
        # Redirect to a success page.
        if 'next' in request.POST:
            return redirect(request.POST.get('next'))
        else:
            return redirect('index')
        
        request.session['userId'] = username
        # return redirect(request.GET.get('next'))
        
    else:
    #     Return an 'invalid login' error message.
        return redirect('/login')
    
def logout(request):
    auth_logout(request)
    request.session.flush()
    return redirect('index')