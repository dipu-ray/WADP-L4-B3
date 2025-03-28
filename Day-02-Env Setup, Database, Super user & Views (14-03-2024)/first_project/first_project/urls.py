from django.contrib import admin
from django.urls import path
from first_project.views import homePage
from first_project.views import contactPage
from first_project.views import productPage
from first_project.views import orderPage
from first_project.views import paymentPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage',homePage,name="homePage"),
    path('contactPage',contactPage,name="contactPage"),
    path('productPage',productPage,name="productPage"),
    path('orderPage',orderPage,name="orderPage"),
    path('paymentPage',paymentPage,name="paymentPage"),
]
