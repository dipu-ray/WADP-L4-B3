from django.shortcuts import render,redirect,HttpResponse
from blogapp.models import BlogModel,AuthorModel,CommentModel,ReviewModel,TagModel

def home(request):
    blog=BlogModel.objects.all()
    myDict={
        'blog':blog
    }
    return render(request,'index.html',myDict)

def author(request):
    author=AuthorModel.objects.all()
    myDict={
        'author':author
    }
    return render(request,'author.html',myDict)

def comment(request):
    comment=CommentModel.objects.all()
    myDict={
        'comment':comment
    }
    return render(request,'comment.html',myDict)

def review(request):
    review=ReviewModel.objects.all()
    myDict={
        'review':review
    }
    return render(request,'review.html',myDict)

def tag(request):
    tag=TagModel.objects.all()
    myDict={
        'tag':tag
    }
    return render(request,'tag.html',myDict)