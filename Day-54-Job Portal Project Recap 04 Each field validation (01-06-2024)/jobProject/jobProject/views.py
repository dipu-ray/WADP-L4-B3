from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from jobApp.models import *
import re

message_box={
    "username_warning":"Username not valid",
    "password_warning":"Password weak",
    "city_warning":"City name not valid",
    "picture_warning":"Image size not valid",
}

def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        role=request.POST.get('role')
        city=request.POST.get('city')
        gender=request.POST.get('gender')
        profile_picture=request.FILES.get('profile_picture')
        email=request.POST.get('email')

        # username validate 
        pattern = r'^[a-z0-9]+$'
        if not re.match(pattern, username):
            messages.warning(request,message_box['username_warning'])
            return redirect('signup')

        # password validate 
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[a-zA-Z0-9@$!%*?&#]+$'
        if not re.match(pattern, password):
            messages.warning(request,message_box['password_warning'])
            return redirect('signup')
        
        # city name validate 
        pattern = r'^[a-zA-Z]+$'
        if not re.match(pattern, city):
            messages.warning(request,message_box['city_warning'])
            return redirect('signup')
        
        # profile image validate 
        max_size_bytes = 5 * 1024 * 1024
        profile_picture.seek(0, 2)  # Move to the end of the file
        file_size = profile_picture.tell()  # Get the current position, which is the file size
        if file_size > max_size_bytes:
            messages.warning(request, message_box['picture_warning'])
            return redirect('signup')
        
        if password==confirm_password:
            user = CustomUserModel.objects.create_user(
                username=username,
                password=password,
                role=role,
                city=city,
                gender=gender,
                profile_picture=profile_picture,
                email=email,
            )
            user.save()
            
            if role=='recruiter':
                role_select=RecruiterModel.objects.create(recruiter_user=user)
              
            else:
                role_select=SeekerModel.objects.create(seeker_user=user)
          
            role_select.save()
            return redirect('signin')
    return render(request,'common/signup.html')

def signin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user_auth = authenticate(
            username=username,
            password=password,
        )
        if user_auth:
            login(request,user_auth)
            return redirect('dashboard')
        
    return render(request,'common/signin.html')

def dashboard(request):
    return render(request,'common/dashboard.html')