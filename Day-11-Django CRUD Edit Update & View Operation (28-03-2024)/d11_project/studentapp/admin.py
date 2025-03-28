from django.contrib import admin
from studentapp.models import studentModel,markModel,teacherModel,subjectModel,universityModel
# Register your models here.

admin.site.register(studentModel)
admin.site.register(markModel)
admin.site.register(teacherModel)
admin.site.register(subjectModel)
admin.site.register(universityModel)