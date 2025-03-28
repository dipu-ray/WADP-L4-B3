from django.contrib import admin
from resumeApp.models import ResumeModel,ResumeEducationModel,ResumeWorkModel
# Register your models here.

admin.site.register(ResumeModel)
admin.site.register(ResumeEducationModel)
admin.site.register(ResumeWorkModel)
