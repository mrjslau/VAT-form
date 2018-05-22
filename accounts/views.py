from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm-password']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Vartotojo vardas užimtas'})
            except:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'errornotsamepass':'Slaptažodžiai turi sutapti'})
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        return render(request, 'accounts/login.html', {'error':'Vartotojo vardas arba/ir slaptažodis neteisingas(-i)'})
    return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
