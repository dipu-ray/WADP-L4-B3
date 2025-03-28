from django.contrib import admin
from django.urls import path
from d6_practise.views import home,news,table,index_page,news2,contact,about,blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('news/',news,name='news'),
    path('table/',table,name='table'),
    path('index/',index_page,name='index'),
    path('news2/',news2,name='news2'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('blog/',blog,name='blog'),
]
