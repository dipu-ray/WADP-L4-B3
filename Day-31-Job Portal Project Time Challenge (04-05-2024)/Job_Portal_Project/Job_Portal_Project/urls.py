from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Job_Portal_Project.views import signup,signin,dashboard,logoutpage,addjob,deletejob,viewsinglejob,profile,editjob,updatejob,appliedjob,postedjob,editprofile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signup,name='signup'),
    path('',signin,name='signin'),
    path('dashboard/',dashboard,name='dashboard'),
    path('logoutpage/',logoutpage,name='logoutpage'),
    path('addjob/',addjob,name='addjob'),
    path('deletejob/<str:myid>',deletejob,name='deletejob'),
    path('viewsinglejob/<str:myid>',viewsinglejob,name='viewsinglejob'),
    path('appliedjob/',appliedjob,name='appliedjob'),
    path('profile/',profile,name='profile'),
    path('editjob/<str:myid>',editjob,name='editjob'),
    path('updatejob/',updatejob,name='updatejob'),
    path('postedjob/',postedjob,name='postedjob'),
    path('editprofile/',editprofile,name='editprofile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
