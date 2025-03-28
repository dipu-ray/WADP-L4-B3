from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # common
    path('signup/',signup,name='signup'),
    path('',signin,name='signin'),
    path('dashboard/',dashboard,name='dashboard'),
    path('logoutpage/',logoutpage,name='logoutpage'),
    path('viewjob/<str:jobid>',viewjob,name='viewjob'),
    path('jobsearch/',jobsearch,name='jobsearch'),
    
    #recruiter
    path('addjob/',addjob,name='addjob'),
    path('joblist/',joblist,name='joblist'),
    path('deletejob/<str:jobid>',deletejob,name='deletejob'),
    path('editjob/<str:jobid>',editjob,name='editjob'),
    
    # seeker
    path('applyjob/<str:jobid>',applyjob,name='applyjob'),
    
    # profile
    path('profile/',profile,name='profile'),
    path('basicinfo/',basicinfo,name='basicinfo'),
    path('seekerinfo/',seekerinfo,name='seekerinfo'),
    path('recruiterinfo/',recruiterinfo,name='recruiterinfo'),
    path('changepassword/',changepassword,name='changepassword'),
    path('editbasicinfo/',editbasicinfo,name='editbasicinfo'),
    path('editseekerprofile/',editseekerprofile,name='editseekerprofile'),
    path('editrecruiterprofile/',editrecruiterprofile,name='editrecruiterprofile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
