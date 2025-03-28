from django.contrib import admin
from django.urls import path
from myProject.views import recruiter,addrecruiter,deleterecruiter,editrecruiter,updaterecruiter,viewrecruiter
urlpatterns = [
    path('admin/', admin.site.urls),
    path('recruiter/',recruiter,name='recruiter'),
    path('addrecruiter/',addrecruiter,name='addrecruiter'),
    path('deleterecruiter/<int:myid>',deleterecruiter,name='deleterecruiter'),
    path('editrecruiter/<int:myid>',editrecruiter,name='editrecruiter'),
    path('updaterecruiter/',updaterecruiter,name='updaterecruiter'),
    path('viewrecruiter/<int:myid>',viewrecruiter,name='viewrecruiter'),
]
