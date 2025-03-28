from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from signInUpProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signupnormal/', signupnormal, name='signupnormal'),
    path('', signinnormal, name='signinnormal'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logoutpage/', logoutpage, name='logoutpage'),
    
    # django form 
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
