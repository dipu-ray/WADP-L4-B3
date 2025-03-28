from django.contrib import admin
from jobportalApp.models import CustomUserModel,JobModel

# Register your models here.

class CustomUserModelDisplay(admin.ModelAdmin):
    list_display=['username','blood_group','user_type']

admin.site.register(CustomUserModel)
admin.site.register(JobModel)