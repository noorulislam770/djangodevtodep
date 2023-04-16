from django.shortcuts import redirect, render
from django.contrib import messages
# Create your views here.


def login(request):
    if request.method == 'POST':
        print("submitted login")
        return redirect('login')
    else:
        return render (request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        print("submitted register ")
        messages.error(request,"Testing error message")
        return redirect('register')
    else:
        return render (request,'accounts/register.html')

def logout():
    return redirect ('index')

def dashboard(request):
    return render (request,'accounts/dashboard.html')