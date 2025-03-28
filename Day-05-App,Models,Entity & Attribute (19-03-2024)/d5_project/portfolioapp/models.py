from django.db import models

# Create your models here.
class PortfolioModel(models.Model):
    project_title=models.CharField(max_length=100)
    project_description=models.CharField(max_length=100)
    project_date=models.CharField(max_length=100)
    
    def __str__(self):
        return self.project_title+' '+self.project_description+' '+self.project_date
    
class ExperienceModel(models.Model):
    company_name=models.CharField(max_length=100)
    job_title=models.CharField(max_length=100)
    employment_duration=models.CharField(max_length=100)
    
    def __str__(self):
        return self.company_name+' '+self.job_title+' '+self.employment_duration
    
class SkillModel(models.Model):
    skill_name=models.CharField(max_length=100)
    skill_category=models.CharField(max_length=100)
    skill_proficiency=models.CharField(max_length=100)
    
    def __str__(self):
        return self.skill_name+' '+self.skill_category+' '+self.skill_proficiency
    
    
class EducationModel(models.Model):
    institution_name=models.CharField(max_length=100)
    degree_obtained=models.CharField(max_length=100)
    graduation_year=models.CharField(max_length=100)
    
    def __str__(self):
        return self.institution_name+' '+self.degree_obtained+' '+self.graduation_year
    
class ProjectCategoryModel(models.Model):
    category_name=models.CharField(max_length=100)
    category_description=models.CharField(max_length=100)
    category_project=models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name+' '+self.category_description+' '+self.category_project