from django.shortcuts import render,redirect,HttpResponse

def home(request):
    return render(request,'index.html')

def news(request):
    return render(request,'news.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')