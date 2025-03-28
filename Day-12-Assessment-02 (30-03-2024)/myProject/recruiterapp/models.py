from django.db import models

# Create your models here.
class recruiterModel(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    job_title=models.CharField(max_length=100)
    linkedin_profile=models.CharField(max_length=100)
    university=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    languages=models.CharField(max_length=100)
    years_of_experience=models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
    