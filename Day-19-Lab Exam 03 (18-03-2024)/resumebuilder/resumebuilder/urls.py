from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from resumebuilder.views import homepage,resumetable,addresume,deleteresume,editresume,updateresume,viewresume,downloadresume

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name='homepage'),
    path('resumetable/',resumetable,name='resumetable'),
    path('addresume/',addresume,name='addresume'),
    path('deleteresume/<str:myid>',deleteresume,name='deleteresume'),
    path('editresume/<str:myid>',editresume,name='editresume'),
    path('updateresume/',updateresume,name='updateresume'),
    path('viewresume/<str:myid>',viewresume,name='viewresume'),
    path('downloadresume/<str:myid>',downloadresume,name='downloadresume'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
