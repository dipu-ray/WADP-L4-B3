from django.db import models

# Create your models here.
class ResumeModel(models.Model):
    Profile_picture=models.ImageField(upload_to='media/ProfilePic')
    Full_name=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Phone_number=models.CharField(max_length=100)
    Email_address=models.CharField(max_length=100)
    Career_objective=models.TextField()
    Hard_Skills=models.CharField(max_length=100)
    Soft_Skills=models.CharField(max_length=100)
    Certifications=models.CharField(max_length=100)
    Projects=models.CharField(max_length=100)
    References=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Full_name
    
class ResumeEducationModel(models.Model):
    Degree=models.CharField(max_length=100)
    Institution=models.CharField(max_length=100)
    Graduation_year=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Institution
    
class ResumeWorkModel(models.Model):
    Company=models.CharField(max_length=100)
    Position=models.CharField(max_length=100)
    Start_dates=models.CharField(max_length=100)
    End_dates =models.CharField(max_length=100)
    
    def __str__(self):
        return self.Company