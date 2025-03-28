from django.contrib import admin
from django.urls import path
from first_project.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pageone/',pageone,name='pageone'),
    path('pagetwo/',pagetwo,name='pagetwo'),
    path('pagethree/',pagethree,name='pagethree'),
    path('pagefour/',pagefour,name='pagefour'),
    path('pagefive/',pagefive,name='pagefive'),
    path('demo/',demo,name='demo'),
    path('home/',home,name='home'),
    path('contact/',contact,name='contact'),
    path('product/',product,name='product'),
    path('order',order,name='order'),
    path('payment',payment,name='payment'),
]
