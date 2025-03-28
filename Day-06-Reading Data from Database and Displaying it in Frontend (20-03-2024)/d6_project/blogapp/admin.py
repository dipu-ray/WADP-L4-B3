from django.contrib import admin
from blogapp.models import BlogModel,AuthorModel,CommentModel,ReviewModel,TagModel
# Register your models here.

admin.site.register(BlogModel)
admin.site.register(AuthorModel)
admin.site.register(CommentModel)
admin.site.register(ReviewModel)
admin.site.register(TagModel)

