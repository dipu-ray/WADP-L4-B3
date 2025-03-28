from django.db import models

# Create your models here.
class aiModel(models.Model):
    ai_name=models.CharField(max_length=100)
    ai_usage=models.CharField(max_length=100)
    ai_category=models.CharField(max_length=100)
    
    def __str__(self):
        return self.ai_name+' '+self.ai_usage+' '+self.ai_category
    
class TaskModel(models.Model):
    task_name=models.CharField(max_length=100)
    task_deadline=models.CharField(max_length=100)
    task_priority=models.CharField(max_length=100)
    
    def __str__(self):
        return self.task_name+' '+self.task_deadline+' '+self.task_priority
    
class DatasetModel(models.Model):
    dataset_name=models.CharField(max_length=100)
    dataset_format=models.CharField(max_length=100)
    dataset_size=models.CharField(max_length=100)
    
    def __str__(self):
        return self.dataset_name+' '+self.dataset_format+' '+self.dataset_size
    
class ExperimentModel(models.Model):
    experiment_name= models.CharField(max_length=100)
    experiment_date= models.CharField(max_length=100)
    experiment_results= models.CharField(max_length=100)
    
    def __str__(self):
        return self.experiment_name+' '+self.experiment_date+' '+self.experiment_results
    
class UserModel(models.Model):
    user_name=models.CharField(max_length=100)
    user_email=models.CharField(max_length=100)
    user_role=models.CharField(max_length=100)
    
    def __str__(self):
        return self.user_name+' '+self.user_email+' '+self.user_role