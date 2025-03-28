from django.db import models

# Create your models here.
class BlogModel(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_author = models.CharField(max_length=100)
    blog_date = models.CharField(max_length=100)
    
    def __str__(self):
        return self.blog_title
    
class AuthorModel(models.Model):
    author_name=models.CharField(max_length=100)
    author_location=models.CharField(max_length=100)
    author_department=models.CharField(max_length=100)
    
    def __str__(self):
        return self.author_name
    
class CommentModel(models.Model):
    comment_text=models.CharField(max_length=100)
    comment_date=models.CharField(max_length=100)
    commenter_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.commenter_name
    
class ReviewModel(models.Model):
    review_rating=models.CharField(max_length=100)
    reviewer_name=models.CharField(max_length=100)
    review_text=models.CharField(max_length=100)
    
    def __str__(self):
        return self.review_text
    
class TagModel(models.Model):
    tag_name=models.CharField(max_length=100)
    tag_category=models.CharField(max_length=100)
    tag_items=models.CharField(max_length=100)
    
    def __str__(self):
        return self.tag_name