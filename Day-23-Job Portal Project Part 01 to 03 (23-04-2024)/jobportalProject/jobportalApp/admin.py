from django.contrib import admin
from jobportalApp.models import CustomUserModel,JobModel
# Register your models here.
class CustomUserModelDisplay(admin.ModelAdmin):
    list_display=['fname','lname','blood_group','user_type']

admin.site.register(CustomUserModel,CustomUserModelDisplay)
admin.site.register(JobModel)