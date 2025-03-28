from django.contrib import admin
from django.urls import path
from d11_practise.views import student,addstudent,deletestudent,editstudent,updatestudent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',student,name='student'),
    path('addstudent/',addstudent,name='addstudent'),
    path('deletestudent/<int:myid>',deletestudent,name='deletestudent'),
    path('editstudent/<int:myid>',editstudent,name='editstudent'),
    path('updatestudent',updatestudent,name='updatestudent'),
]
