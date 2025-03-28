from django.contrib import admin
from jobportalApp.models import CustomUserModel

# Register your models here.
class Custom_User_Display(admin.ModelAdmin):
    list_display=['display_name','user_name','email']

admin.site.register(CustomUserModel,Custom_User_Display)