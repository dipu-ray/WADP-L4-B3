from django.shortcuts import render,redirect,HttpResponse

def pageone(request):
    return HttpResponse('This is page one')

def pagetwo(request):
    return HttpResponse('This is page two')

def pagethree(request):
    return HttpResponse('This is page three')

def pagefour(request):
    return HttpResponse('This is page four')

def pagefive(request):
    return HttpResponse('This is page five')

def demo(request):
    return render(request,'demo.html')

def home(request):
    mydict={
        'page_title':'Google',
        'url':'https://google.com',
        'last_updated':'16-03-2024'
    }
    return render(request,'home.html',mydict)

def contact(request):
    mydict={
        'name':'Tansen',
        'phone':'235236234',
        'email':'aatansen@gmail.com',
    }
    return render(request,'contact.html',mydict)

def product(request):
    mydict={
        'product_name':'Iphone',
        'price':'452356236',
        'category':'mobile',
    }
    return render(request,'product.html',mydict)

def order(request):
    mydict={
        'order_id':'14523',
        'customer_id':'4335345',
        'order_date':'16-03-2024',
    }
    return render(request,'order.html',mydict)

def payment(request):
    mydict={
        'payment_id':'3423',
        'order_id':'3346342',
        'payment_amount':'356235632'
    }
    return render(request,'payment.html',mydict)