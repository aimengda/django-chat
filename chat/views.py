from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView



# Create your views here.
def user_login(request):
    if request.method == 'GET':
        return render(request, 'chat/login.html')
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/homepage')
        else:
            return HttpResponse("invalid login")

class Register(CreateView):
    model = User
    fields = ['email','username', 'first_name', 'last_name', 'password']
    template_name = 'chat/register.html'
    success_url = '/login'

def user_logout(request):
    logout(request)
    return redirect('/login')

def homepage(request):
    return render(request,'chat/homepage.html')
