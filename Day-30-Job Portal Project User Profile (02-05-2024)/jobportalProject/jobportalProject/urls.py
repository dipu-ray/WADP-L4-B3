from django.contrib import admin
from django.urls import path
from jobportalProject.views import signup,signin,dashboard,logoutpage,profile,addjob,editjob,updatejob,deletejob,viewsinglejob,viewalljob,editprofile,updateprofile,postedjob
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signup,name='signup'),
    path('',signin,name='signin'),
    path('dashboard/',dashboard,name='dashboard'),
    path('logoutpage/',logoutpage,name='logoutpage'),
    path('profile/',profile,name='profile'),
    path('addjob/',addjob,name='addjob'),
    path('editjob/<str:myid>',editjob,name='editjob'),
    path('updatejob/',updatejob,name='updatejob'),
    path('deletejob/<str:myid>',deletejob,name='deletejob'),
    path('viewsinglejob/<str:myid>',viewsinglejob,name='viewsinglejob'),
    path('viewalljob/',viewalljob,name='viewalljob'),
    path('editprofile/',editprofile,name='editprofile'),
    path('updateprofile/',updateprofile,name='updateprofile'),
    path('postedjob/',postedjob,name='postedjob'),
]
