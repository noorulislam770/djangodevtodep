from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,"You are now logged in . ")
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid Credentials. ")
            return redirect('login')

    else:
        return render (request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username is taken. ")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.error(request,"Email is already registered. ")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                # auth.login(request,user)
                # messages.success(request, "You are now logged in  ")
                # return redirect('index')
                user.save()
                messages.success(request, "You are now Registerd and can log in  ")
                return redirect('login')


        else:
            messages.error(request,"Passwords Do not match ")
            return redirect('register')
    else:
        return render (request,'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,"You have been Logged Out.")
        return redirect('index')

def dashboard(request):
    return render (request,'accounts/dashboard.html')