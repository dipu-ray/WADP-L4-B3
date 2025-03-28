from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from d14_project.views import student,addstudent,mark,addmark,teacher,addteacher,subject,addsubject,university,adduniversity,deleteMark,deleteStudent,deleteSubject,deleteTeacher,deleteUniversity,viewstudent,viewteacher,viewmark,viewsubject,viewuniversity,alltable,editstudent,updatestudent
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
    path('deleteMark/<str:myid>',deleteMark,name='deleteMark'),
    path('deleteStudent/<str:myid>',deleteStudent,name='deleteStudent'),
    path('deleteSubject/<str:myid>',deleteSubject,name='deleteSubject'),
    path('deleteTeacher/<str:myid>',deleteTeacher,name='deleteTeacher'),
    path('deleteUniversity/<str:myid>',deleteUniversity,name='deleteUniversity'),
    path('viewstudent/<int:myid>',viewstudent,name='viewstudent'),
    path('viewteacher/<int:myid>',viewteacher,name='viewteacher'),
    path('viewmark/<int:myid>',viewmark,name='viewmark'),
    path('viewsubject/<int:myid>',viewsubject,name='viewsubject'),
    path('viewuniversity/<int:myid>',viewuniversity,name='viewuniversity'),
    path('alltable/',alltable,name='alltable'),
    path('editstudent/<int:myid>',editstudent,name='editstudent'),
    path('updatestudent',updatestudent,name='updatestudent'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
