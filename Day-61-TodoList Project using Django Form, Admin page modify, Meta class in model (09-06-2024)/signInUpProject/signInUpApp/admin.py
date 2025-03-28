from django.contrib import admin
from .models import *

# Register your models here.

class CustomUserModelDisplay(admin.ModelAdmin):
    list_display=['username','User_Type','City']
    search_fields=['username','User_Type','City']
    
    fieldsets=[
        (
            'User Info',
            {
                'fields':['username','email','password']
            },
        ),
        (
            'Advanced Options',
            {
                'classes':['collapse'],
                'fields':['first_name','last_name','City','Profile_Picture','User_Type']
            }
        )
    ]
    
admin.site.register(CustomUserModel,CustomUserModelDisplay)
