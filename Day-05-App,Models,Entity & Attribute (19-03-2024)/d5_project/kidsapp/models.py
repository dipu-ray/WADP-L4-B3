from django.db import models

# Create your models here.
class KidModel(models.Model):
    kid_name=models.CharField(max_length=100)
    kid_age=models.CharField(max_length=100)
    kid_gender=models.CharField(max_length=100)
    
    def __str__(self):
        return self.kid_name+' '+self.kid_age+' '+self.kid_gender
    
class ToyModel(models.Model):
    toy_name=models.CharField(max_length=100)
    toy_category=models.CharField(max_length=100)
    toy_price=models.CharField(max_length=100)
    
    def __str__(self):
        return self.toy_name+' '+self.toy_category+' '+self.toy_price
    
class RatingModel(models.Model):
    rating_value=models.CharField(max_length=100)
    rating_date=models.CharField(max_length=100)
    reviewer_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.rating_value+' '+self.rating_date+' '+self.reviewer_name
    
class ManufacturerModel(models.Model):
    manufacturer_name=models.CharField(max_length=100)
    manufacturer_location=models.CharField(max_length=100)
    manufacturer_contact=models.CharField(max_length=100)
    
    def __str__(self):
        return self.manufacturer_name+' '+self.manufacturer_location+' '+self.manufacturer_contact
    
class LocationModel(models.Model):
    location_name=models.CharField(max_length=100)
    location_description=models.CharField(max_length=100)
    location_address=models.CharField(max_length=100)
    
    def __str__(self):
        return self.location_name+' '+self.location_description+' '+self.location_address