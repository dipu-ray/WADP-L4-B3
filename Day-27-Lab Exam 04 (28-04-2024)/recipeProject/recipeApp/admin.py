from django.contrib import admin
from recipeApp.models import CustomUserModel,RecipeModel
# Register your models here.

class CustomUserModelDisplay(admin.ModelAdmin):
    list_display=['username','user_type','gender']

admin.site.register(CustomUserModel,CustomUserModelDisplay)
admin.site.register(RecipeModel)
