from django.db import models

# Create your models here.
class studentModel(models.Model):
    Name=models.CharField(max_length=100,null=True)
    Department=models.CharField(max_length=100,null=True)
    City=models.CharField(max_length=100,null=True)
    StudentImage=models.ImageField(upload_to='media/StudentImages',null=True)
    
    def __str__(self):
        return self.Name

class markModel(models.Model):
    Name=models.CharField(max_length=100)
    Roll=models.CharField(max_length=100)
    Mark=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name
    
class teacherModel(models.Model):
    Name=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name
    
class subjectModel(models.Model):
    Name=models.CharField(max_length=100)
    Category=models.CharField(max_length=100)
    Mark=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name
    
class universityModel(models.Model):
    Rank=models.CharField(max_length=100)
    Name=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name