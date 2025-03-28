from django.db import models

# Create your models here.
class BlogModel(models.Model):
    blog_title=models.CharField(max_length=100)
    blog_date=models.CharField(max_length=100)
    blog_category=models.CharField(max_length=100)
    
    def __str__(self):
        return self.blog_title+' '+self.blog_date+' '+self.blog_category
    
class NewsModel(models.Model):
    news_headings=models.CharField(max_length=100)
    news_date=models.CharField(max_length=100)
    news_category=models.CharField(max_length=100)
    
    def __str__(self):
        return self.news_headings+' '+self.news_date+' '+self.news_category
    
class CommentModel(models.Model):
    comment_text = models.CharField(max_length=100)
    comment_date = models.CharField(max_length=100)
    commenter_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.comment_text+' '+self.comment_date+' '+self.commenter_name
    
class AuthorModel(models.Model):
    author_name = models.CharField(max_length=100)
    author_bio = models.CharField(max_length=100)
    author_email = models.CharField(max_length=100)
    
    def __str__(self):
        return self.author_name+' '+self.author_bio+' '+self.author_email
    
class TagModel(models.Model):
    tag_name=models.CharField(max_length=100)
    tag_description=models.CharField(max_length=100)
    tag_items=models.CharField(max_length=100)
    
    def __str__(self):
        return self.tag_name+' '+self.tag_description+' '+self.tag_items