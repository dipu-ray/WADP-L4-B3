from django.shortcuts import render,redirect,HttpResponse

def homePage(request):
    return HttpResponse("This is homePage")
def contactPage(request):
    return HttpResponse("This is contactPage")
def productPage(request):
    return HttpResponse("This is productPage")
def orderPage(request):
    return HttpResponse("This is orderPage")
def paymentPage(request):
    return HttpResponse("This is paymentPage")