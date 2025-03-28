from django.contrib import admin
from django.urls import path
from myApp.views import StudentList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('StudentList/',StudentList.as_view(),name='StudentList')
]
