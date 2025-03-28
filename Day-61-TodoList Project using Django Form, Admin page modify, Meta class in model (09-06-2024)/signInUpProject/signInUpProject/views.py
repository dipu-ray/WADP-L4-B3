from django.shortcuts import render,redirect
from signInUpApp.models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from signInUpProject.forms import CustomUserForm,CustomAuthForm
from django.contrib import messages

all_messages={
    'signup_success':'Sign up successful!',
    'signin_success':'Sign in successful!',
}


def signupnormal(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        City=request.POST.get('City')
        Profile_Picture=request.FILES.get('Profile_Picture')
        User_Type=request.POST.get('User_Type')
        
        if password==confirm_password:
            user = CustomUserModel.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
                City=City,
                Profile_Picture=Profile_Picture,
                User_Type=User_Type
            )
            user.save()
            messages.success(request,all_messages['signup_success'])
            return redirect('signinnormal')
    return render(request,'common/signupnormal.html')

def signinnormal(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(
            username=username,
            password=password,
        )
        if user:
            login(request,user)
            messages.success(request,all_messages['signin_success'])
            return redirect('dashboard')
        
    return render(request,'common/signinnormal.html')

@login_required
def dashboard(request):
    return render(request,'common/dashboard.html')

@login_required
def logoutpage(request):
    logout(request)
    return redirect('signinnormal')

def signup(request):
    if request.method=="POST":
        form=CustomUserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,all_messages['signup_success'])
            return redirect('signin')
    
    else:
        form=CustomUserForm()
    return render(request,'common/signup.html',{'form':form})

def signin(request):
    if request.method=="POST":
        form=CustomAuthForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request,all_messages['signin_success'])
            return redirect('dashboard')
    else:
        form=CustomAuthForm()
    return render(request,'common/signin.html',{'form':form})