from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    picture = models.ImageField(upload_to='static/profilePic')
    dob = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=100)
    BLOOD_GROUP=[
        ('a+','A Positive'),
        ('a-','A Negative'),
        ('b+','B Positive'),
        ('b-','B Negative'),
        ('c+','C Positive'),
        ('c-','C Negative'),
        ('ab+','AB Positive'),
        ('ab-','AB Negative'),
        ('o+','O Positive'),
        ('o-','O Negative'),
    ]
    blood_group = models.CharField(choices=BLOOD_GROUP,max_length=100)
    USER_TYPE=[
        ('recruiter','Job Recruiter'),
        ('seeker','Job Seeker'),
    ]
    user_type=models.CharField(choices=USER_TYPE,max_length=100)

    def __str__(self):
        return self.username
    
class JobModel(models.Model):
    Job_title=models.CharField(max_length=100)
    Company_name=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Company_description=models.TextField()
    Job_description=models.TextField()
    Qualification=models.CharField(max_length=100)
    Salary_information=models.CharField(max_length=100)
    Deadline=models.DateField(auto_now_add=True)
    Designation=models.CharField(max_length=100)
    Experience=models.CharField(max_length=100)
    Created_by=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.Job_title} created by {self.Created_by}"
    
class JobSeekerProfile(models.Model):
    user = models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='jobseekerprofile')
    skills=models.CharField(max_length=100)
    work_experience=models.CharField(max_length=100)

    def __str__(self):
        return self.user.user_type

class JobRecruiterProfile(models.Model):
    user = models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='jobrecruiterprofile')
    Skills_Required = models.CharField(max_length=200)
    Work_Schedule = models.CharField(max_length=50)
    def __str__(self):
        return self.user.user_type