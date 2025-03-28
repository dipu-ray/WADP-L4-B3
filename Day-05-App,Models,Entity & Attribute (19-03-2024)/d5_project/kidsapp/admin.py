from django.contrib import admin
from kidsapp.models import KidModel,ToyModel,RatingModel,ManufacturerModel,LocationModel

# Register your models here.

admin.site.register(KidModel)
admin.site.register(ToyModel)
admin.site.register(RatingModel)
admin.site.register(ManufacturerModel)
admin.site.register(LocationModel)
