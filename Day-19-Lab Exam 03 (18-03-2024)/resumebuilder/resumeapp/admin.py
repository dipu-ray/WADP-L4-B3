from django.contrib import admin
from resumeapp.models import ResumeModel,EducationModel,WorkModel

# Register your models here.
admin.site.register(ResumeModel)
admin.site.register(EducationModel)
admin.site.register(WorkModel)
