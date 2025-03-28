from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signin,name='signin'),
    path('dashboard/',dashboard,name='dashboard'),
]
