from django.db import models

# Create your models here.
class ProductModel(models.Model):
    product_name=models.CharField(max_length=100)
    product_price=models.CharField(max_length=100)
    product_quantity=models.CharField(max_length=100)
    
    def __str__(self):
        return self.product_name+' '+self.product_price+' '+self.product_quantity
    
class OrderModel(models.Model):
    order_number=models.CharField(max_length=100)
    order_date=models.CharField(max_length=100)
    customer_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.order_number+' '+self.order_date+' '+self.customer_name
    
class ReviewModel(models.Model):
    review_text=models.CharField(max_length=100)
    review_date=models.CharField(max_length=100)
    product_id=models.CharField(max_length=100)
    
    def __str__(self):
        return self.review_text+' '+self.review_date+' '+self.product_id
    
class SellerModel(models.Model):
    seller_name=models.CharField(max_length=100)
    seller_email=models.CharField(max_length=100)
    seller_location=models.CharField(max_length=100)
    
    def __str__(self):
        return self.seller_name+' '+self.seller_email+' '+self.seller_location
    
class PaymentModel(models.Model):
    payment_method=models.CharField(max_length=100)
    payment_date=models.CharField(max_length=100)
    payment_amount=models.CharField(max_length=100)
    
    def __str__(self):
        return self.payment_method+' '+self.payment_date+' '+self.payment_amount