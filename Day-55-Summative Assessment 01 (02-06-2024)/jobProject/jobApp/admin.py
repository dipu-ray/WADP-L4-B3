from django.contrib import admin
from jobApp.models import *
# Register your models here.
admin.site.register(CustomUserModel)
admin.site.register(RecruiterModel)
admin.site.register(SeekerModel)
admin.site.register(SeekerEducationModel)
admin.site.register(SeekerWorkModel)
admin.site.register(JobModel)
