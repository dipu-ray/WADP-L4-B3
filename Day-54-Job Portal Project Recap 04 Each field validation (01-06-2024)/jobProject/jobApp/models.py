from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    ROLE={
        ('recruiter','Job Recruiter'),
        ('seeker','Job Seeker'),
    }
    role=models.CharField(choices=ROLE,max_length=100)
    city=models.CharField(max_length=100)
    
    GENDER={
        ('male','Male'),
        ('female','Female'),
        ('others','Others'),
    }
    gender=models.CharField(choices=GENDER,max_length=100)
    profile_picture=models.ImageField(upload_to='media/profile_picture')
    
    # basic info
    father_name=models.CharField(max_length=100)
    mother_name=models.CharField(max_length=100)
    hobby=models.CharField(max_length=100)
    
    def __str__(self):
        return self.username

class RecruiterModel(models.Model):
    # contact info 
    mobile_number = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    recruiter_user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='recruitermodel')
    def __str__(self):
        return self.recruiter_user.username

class SeekerModel(models.Model):
    edu_qualification=models.CharField(max_length=100)
    work_experience=models.CharField(max_length=100)
    seeker_user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='seekermodel')
    def __str__(self):
        return self.seeker_user.username

