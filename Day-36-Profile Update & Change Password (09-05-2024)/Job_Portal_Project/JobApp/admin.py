from django.contrib import admin
from JobApp.models import CustomUserModel,JobModel,RecruiterProfileModel,SeekerProfileModel,RecruiterBasicInfoModel,RecruiterContactModel,SeekerBasicInfoModel,SeekerContactModel,SeekerEducationModel,SeekerWorkExModel

# Register your models here.

class CustomUserModelDisplay(admin.ModelAdmin):
    list_display=['username','user_types','blood_group']

admin.site.register(CustomUserModel,CustomUserModelDisplay)
admin.site.register(JobModel)
admin.site.register(RecruiterProfileModel)
admin.site.register(SeekerProfileModel)

# after template mastering:
admin.site.register(RecruiterBasicInfoModel)
admin.site.register(RecruiterContactModel)
admin.site.register(SeekerBasicInfoModel)
admin.site.register(SeekerContactModel)
admin.site.register(SeekerEducationModel)
admin.site.register(SeekerWorkExModel)
