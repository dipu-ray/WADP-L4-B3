from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUserModel(AbstractUser):
    profile_photo = models.ImageField(upload_to="static/profile_pic")
    age = models.CharField(max_length=100)
    
    GENDER=[
        ('male','Male'),
        ('female','Female'),
    ]
    
    gender = models.CharField(choices=GENDER,max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    BLOOF_GROUP=[
        ('a+','A Positive'),
        ('b+','B Positive'),
        ('ab+','AB Positive'),
        ('o+','O Positive'),
    ]

    blood_group = models.CharField(choices=BLOOF_GROUP,max_length=100)

    USER_TYPES=[
        ('recruiter','Recruiter'),
        ('seeker','Seeker'),
    ]
    user_types = models.CharField(choices=USER_TYPES,max_length=100)

    def __str__(self):
        return self.username
    
class JobModel(models.Model):
    Company_logo=models.ImageField(upload_to='static/company_logo')
    Job_title=models.CharField(max_length=100)
    Job_description=models.TextField()
    Job_location=models.CharField(max_length=100)
    Requirements=models.TextField()
    Qualifications=models.CharField(max_length=100)
    JOB_TYPES=[
        ('full_time','Full time'),
        ('part_time','Part time'),
    ]
    Job_types=models.CharField(choices=JOB_TYPES,max_length=100)
    WORKPLACE=[
        ('remote','Remote'),
        ('On_site','On-site'),
    ]
    Workplace=models.CharField(choices=WORKPLACE,max_length=100)
    Salary=models.CharField(max_length=100)
    Experience=models.CharField(max_length=100)
    Deadline=models.DateField(auto_now_add=True)
    Created_by = models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.Created_by.username
    
class RecruiterProfileModel(models.Model):
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='recruiterprofilemodel')
    Company_name=models.CharField(max_length=100)
    Company_location=models.CharField(max_length=100)
    Recruiter_Name=models.CharField(max_length=100)
    def __str__(self):
        return self.user.username

class SeekerProfileModel(models.Model):
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='seekerprofilemodel')
    Qualification=models.CharField(max_length=100)
    Experience=models.CharField(max_length=100)
    Skills=models.CharField(max_length=100)
    LAST_EDUCATION=[
        ('jsc','JSC'),
        ('ssc','SSC'),
        ('hsc','HSC'),
    ]
    last_education = models.CharField(choices=LAST_EDUCATION,max_length=100)

    def __str__(self):
        return self.user.username

#after template mastering:
class RecruiterBasicInfoModel(models.Model):
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='recruiterbasicinfomodel')
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    hobby = models.CharField(max_length=100)
    languages = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class RecruiterContactModel(models.Model):
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='recruitercontactmodel')
    mobile_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class SeekerBasicInfoModel(models.Model):
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='seekerbasicinfomodel')
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    hobby = models.CharField(max_length=100)
    languages = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    
class SeekerContactModel(models.Model):
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='seekercontactmodel')
    mobile_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class SeekerEducationModel(models.Model):
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='seekereducationmodel')
    education_name=models.CharField(max_length=100)
    education_year=models.CharField(max_length=100)
    education_institute=models.CharField(max_length=100)
    def __str__(self):
        return self.user.username

class SeekerWorkExModel(models.Model):
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='seekerworkexmodel')
    Position=models.CharField(max_length=100)
    Company_name=models.CharField(max_length=100)
    Duration=models.CharField(max_length=100)

    def __str__(self):
        return self.user.username



