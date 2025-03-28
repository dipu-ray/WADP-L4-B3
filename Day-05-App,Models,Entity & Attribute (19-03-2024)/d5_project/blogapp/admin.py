from django.contrib import admin
from blogapp.models import BlogModel,NewsModel,CommentModel,AuthorModel,TagModel
# Register your models here.
admin.site.register(BlogModel)
admin.site.register(NewsModel)
admin.site.register(CommentModel)
admin.site.register(AuthorModel)
admin.site.register(TagModel)