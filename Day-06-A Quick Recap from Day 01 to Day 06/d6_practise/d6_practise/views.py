from django.shortcuts import render,redirect,HttpResponse
from blogapp.models import blogModel

def home(request):
    return HttpResponse('this is simple text')

def news(request):
    return render(request,'news.html')

def table(request):
    myDict={
        'name':'Shakil',
        'department':'EEE',
        'city':'Barisal',
    }
    return render(request,'table.html',myDict)

def index_page(request):
    return render(request,'index.html')

def news2(request):
    return render(request,'news2.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def blog(request):
    blog = blogModel.objects.all()
    myDict={
        'blog':blog
    }
    return render(request,'blog.html',myDict)