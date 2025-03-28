from django.contrib import admin
from jobportalApp.models import CustomUserModel
# Register your models here.

class Custom_User_Display(admin.ModelAdmin):
    list_display=['fname','usertype','blood_group','date_of_birth']

admin.site.register(CustomUserModel,Custom_User_Display)
