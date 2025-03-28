from django.contrib import admin
from django.urls import path
from d9_project.views import student,addstudent,mark,addmark,teacher,addteacher,subject,addsubject,university,adduniversity
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',student,name='student'),
    path('addstudent/',addstudent,name='addstudent'),
    path('mark/',mark,name='mark'),
    path('addmark/',addmark,name='addmark'),
    path('teacher/',teacher,name='teacher'),
    path('addteacher/',addteacher,name='addteacher'),
    path('subject/',subject,name='subject'),
    path('addsubject/',addsubject,name='addsubject'),
    path('university/',university,name='university'),
    path('adduniversity/',adduniversity,name='adduniversity'),
    
]
