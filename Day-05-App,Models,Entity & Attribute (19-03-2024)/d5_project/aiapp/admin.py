from django.contrib import admin
from aiapp.models import aiModel,TaskModel,DatasetModel,ExperimentModel,UserModel

# Register your models here.
admin.site.register(aiModel)
admin.site.register(TaskModel)
admin.site.register(DatasetModel)
admin.site.register(ExperimentModel)
admin.site.register(UserModel)