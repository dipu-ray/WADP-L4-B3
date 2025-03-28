from django.shortcuts import render, redirect

def signuppage(request):
    return render(request,'signuppage.html')

def signinpage(request):
    return render(request,'signinpage.html')