from django.contrib import admin
from django.urls import path
from d6_project.views import home,author,comment,review,tag

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('author/',author,name='author'),
    path('comment/',comment,name='comment'),
    path('review/',review,name='review'),
    path('tag/',tag,name='tag'),
]
