from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Job_Portal_Project.views import signup,signin,dashboard,logoutpage,addjob,deletejob,viewsinglejob,profile,editjob,updatejob,appliedjob,postedjob,editprofile,profiles_info,recruiterbasicinfo,recruitercontact,seekerbasicinfo,seekercontact,seekereducation,seekerworkex,updateprofile,changepassword

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signup,name='signup'),
    path('',signin,name='signin'),
    path('dashboard/',dashboard,name='dashboard'),
    path('logoutpage/',logoutpage,name='logoutpage'),
    path('addjob/',addjob,name='addjob'),
    path('deletejob/<str:myid>',deletejob,name='deletejob'),
    path('viewsinglejob/<str:myid>',viewsinglejob,name='viewsinglejob'),
    path('editjob/<str:myid>',editjob,name='editjob'),
    path('profile/',profile,name='profile'),
    path('profile/appliedjob/',appliedjob,name='appliedjob'),
    path('updatejob/',updatejob,name='updatejob'),
    path('profile/postedjob/',postedjob,name='postedjob'),
    path('profile/editprofile/',editprofile,name='editprofile'),
    path('profile/profiles_info/',profiles_info,name='profiles_info'),
    path('profile/recruiterbasicinfo/',recruiterbasicinfo,name='recruiterbasicinfo'),
    path('profile/recruitercontact/',recruitercontact,name='recruitercontact'),
    path('profile/seekerbasicinfo/',seekerbasicinfo,name='seekerbasicinfo'),
    path('profile/seekercontact/',seekercontact,name='seekercontact'),
    path('profile/seekereducation/',seekereducation,name='seekereducation'),
    path('profile/seekerworkex/',seekerworkex,name='seekerworkex'),
    path('updateprofile/',updateprofile,name='updateprofile'),
    path('changepassword/',changepassword,name='changepassword'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
