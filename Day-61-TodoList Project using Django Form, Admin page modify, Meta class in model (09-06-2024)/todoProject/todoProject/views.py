from django.shortcuts import render,redirect
from todoApp.models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import login,logout

all_messages={
    'signup_success':'Signup successful!',
    'signin_success':'Signin successful!',
}

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, all_messages['signup_success'])
            return redirect('signin')
    else:
        form = CustomUserCreationForm()

    return render(request, 'common/signup.html', {'form': form})
            

def signin(request):
    if request.method=="POST":
        form=CustomUserAuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            messages.success(request,all_messages['signin_success'])
            return redirect('dashboard')
    else:
        form=CustomUserAuthenticationForm()
    return render(request,'common/signin.html',{'form':form})

def dashboard(request):
    return render(request,'common/dashboard.html')

def logoutpage(request):
    logout(request)
    return redirect('signin')