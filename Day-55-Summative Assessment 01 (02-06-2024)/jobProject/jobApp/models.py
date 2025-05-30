from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    USER_TYPE={
        ('seeker','Job Seeker'),
        ('recruiter','Job Recruiter'),
    }
    user_type=models.CharField(choices=USER_TYPE,max_length=100)
    city=models.CharField(max_length=100)
    GENDER={
        ('male','Male'),
        ('female','Female'),
        ('others','Others'),
    }    
    gender=models.CharField(choices=GENDER,max_length=100)
    profile_picture=models.ImageField(upload_to='media/profile_picture')

    def __str__(self):
        return self.username

class RecruiterModel(models.Model):
    # basic_info 
    company_name=models.CharField(max_length=100)
    company_location=models.CharField(max_length=100)
    company_details=models.CharField(max_length=100)
    
    # contact
    mobile_number=models.CharField(max_length=100)
    company_address=models.CharField(max_length=100)
    
    recruiter_user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='recruitermodel')
    
    def __str__(self):
        return self.recruiter_user.username
    
class SeekerModel(models.Model):
    # basic_info
    father_name=models.CharField(max_length=100)
    mother_name=models.CharField(max_length=100)
    hobby=models.CharField(max_length=100)
    seeker_user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='seekermodel')
    def __str__(self):
        return self.seeker_user.username
class SeekerEducationModel(models.Model):
    # education
    edu_name=models.CharField(max_length=100)
    edu_institute=models.CharField(max_length=100)
    edu_location=models.CharField(max_length=100)
    seeker_user=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,related_name='seekeredumodel')
    def __str__(self):
        return self.seeker_user.username
class SeekerWorkModel(models.Model):
    # work exprerience
    work_name=models.CharField(max_length=100)
    work_location=models.CharField(max_length=100)
    work_time=models.CharField(max_length=100)
    seeker_user=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,related_name='seekereorkmodel')

    def __str__(self):
        return self.seeker_user.username
    
class JobModel(models.Model):
    job_title=models.CharField(max_length=100)
    company_description=models.TextField()
    company_logo=models.ImageField(upload_to='media/company_logo')
    company_name=models.CharField(max_length=100)
    company_location=models.TextField()
    qualifications=models.CharField(max_length=100)
    deadline=models.DateField()
    salary=models.CharField(max_length=100)
    created_by=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.created_by.username
    
    