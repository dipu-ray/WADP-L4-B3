from django.contrib import admin
from JobApp.models import CustomUserModel,JobModel,RecruiterProfileModel,SeekerProfileModel

# Register your models here.

class CustomUserModelDisplay(admin.ModelAdmin):
    list_display=['username','user_types','blood_group']

admin.site.register(CustomUserModel,CustomUserModelDisplay)
admin.site.register(JobModel)
admin.site.register(RecruiterProfileModel)
admin.site.register(SeekerProfileModel)