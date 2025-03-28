from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(
            username=username,
            password=password,
        )
        if user:
            login(request,user)
            return redirect('dashboard')
    return render(request,'signin.html')

def dashboard(request):
    return render(request,'dashboard.html')