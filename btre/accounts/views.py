from django.shortcuts import redirect, render

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
        return redirect('login')
    else:
        return render (request,'accounts/register.html')

def logout():
    return redirect ('index')

def dashboard(request):
    return render (request,'accounts/dashboard.html')