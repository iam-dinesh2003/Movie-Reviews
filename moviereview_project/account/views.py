from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('User login successful')
            return redirect('/')
        else:
            print('User login failed')
    return render(request, 'account/login.html')

def logoutt(request):
    logout(request)
    return redirect("/account/login")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('/account/login')
    return render(request, 'account/register.html')