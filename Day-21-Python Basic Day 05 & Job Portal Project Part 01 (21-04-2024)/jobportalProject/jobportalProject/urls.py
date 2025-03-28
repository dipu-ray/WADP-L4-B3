from django.contrib import admin
from django.urls import path
from jobportalProject.views import signuppage,signinpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signuppage/',signuppage,name='signuppage'),
    path('',signinpage,name='signinpage'),
]
