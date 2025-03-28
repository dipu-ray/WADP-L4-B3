from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUserModel(AbstractUser):
    GENDER=[
        ('male','Male'),
        ('female','Female'),
    ]
    gender=models.CharField(choices=GENDER,max_length=50)
    age=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    USER_TYPE=[
        ('chef','Chef'),
        ('viewer','Viewer'),
    ]
    user_type=models.CharField(choices=USER_TYPE,max_length=50)

    def __str__(self):
        return self.username
    
class RecipeModel(models.Model):
    recipe_title=models.CharField(max_length=100)
    ingredients=models.TextField()
    Instructions=models.TextField()
    preparation_time=models.CharField(max_length=100)
    cooking_time=models.CharField(max_length=100)
    total_time=models.CharField(max_length=100)
    
    DIFFICULTY_LEVEL=[
        ('low','Low'),
        ('medium','Medium'),
        ('high','High'),
    ]
    
    difficulty_level=models.CharField(choices=DIFFICULTY_LEVEL,max_length=50)
    nutritional_info=models.TextField()
    recipe_image=models.ImageField(upload_to='static/recipe_image')
    RECIPE_CATEGORY=[
        ('breakfast','Breakfast'),
        ('launch','Launch'),
        ('dinner','Dinner'),
    ]
    recipe_category=models.CharField(choices=RECIPE_CATEGORY,max_length=50)
    USER_TAGS=[
        ('vegetarian','Vegetarian'),
        ('non-vegetarian','Non Vegetarian'),
    ]
    user_tags=models.CharField(choices=USER_TAGS,max_length=50)
    total_calorie=models.CharField(max_length=40)
    created_by=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.recipe_title} created by {self.created_by}"

class ChefProfileModel(models.Model):
    myuser = models.OneToOneField(CustomUserModel,on_delete=models.CASCADE)
    experience=models.CharField(max_length=100)
    skill=models.CharField(max_length=100)
    resume_latter=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to='static/profile_pic')

    def __str__(self):
        return self.myuser.username

class ViewerProfileModel(models.Model):
    myuser = models.OneToOneField(CustomUserModel,on_delete=models.CASCADE)
    favourite=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to='static/profile_pic')

    def __str__(self):
        return self.myuser.username