from django.contrib import admin
from django.urls import path
from d4_project.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('news/',news,name='news'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
]
