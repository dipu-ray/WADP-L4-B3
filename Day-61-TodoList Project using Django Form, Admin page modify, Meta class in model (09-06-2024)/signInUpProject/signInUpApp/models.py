from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUserModel(AbstractUser):
    City=models.CharField(max_length=100,null=True)
    Profile_Picture=models.ImageField(upload_to='media/Profile_Picture',null=True)
    
    USER_TYPE={
        ('user','User'),
        ('admin','Admin'),
    }
    
    User_Type=models.CharField(choices=USER_TYPE,max_length=100,null=True)
    
    def __str__(self):
        return self.username
