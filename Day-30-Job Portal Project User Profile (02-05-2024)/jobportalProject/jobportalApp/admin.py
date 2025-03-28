from django.contrib import admin
from jobportalApp.models import CustomUserModel,JobModel,JobRecruiterProfile,JobSeekerProfile
# Register your models here.

class CustomUserModelDisplay(admin.ModelAdmin):
    list_display=['username','user_type','blood_group']

admin.site.register(CustomUserModel,CustomUserModelDisplay)
admin.site.register(JobModel)
admin.site.register(JobRecruiterProfile)
admin.site.register(JobSeekerProfile)
