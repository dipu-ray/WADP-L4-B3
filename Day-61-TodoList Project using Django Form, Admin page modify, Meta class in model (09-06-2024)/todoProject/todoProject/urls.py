from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from todoProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signup,name='signup'),
    path('',signin,name='signin'),
    path('dashboard/',dashboard,name='dashboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)