from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUserModel(AbstractUser):
    USER=[
        ('recruiter','Recruiter'),
        ('seeker','Seeker'),
    ]
    BLOOD_GROUP=[
        ('A+', 'A positive'),
        ('A-', 'A negative'),
        ('B+', 'B positive'),
        ('B-', 'B negative'),
        ('AB+', 'AB positive'),
        ('AB-', 'AB negative'),
        ('O+', 'O positive'),
        ('O-', 'O negative'),
    ]

    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    profile_picture=models.ImageField(upload_to='media/profilePic')
    # date_of_birth=models.DateField(auto_now=True)
    date_of_birth=models.DateField(auto_now_add=True)
    address=models.CharField(max_length=100)
    blood_group=models.CharField(choices=BLOOD_GROUP,max_length=100)
    usertype=models.CharField(choices=USER,max_length=100)

    def __str__(self):
        return self.fname


