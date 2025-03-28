from django.contrib import admin
from portfolioapp.models import PortfolioModel,ExperienceModel,SkillModel,EducationModel,ProjectCategoryModel
# Register your models here.

admin.site.register(PortfolioModel)
admin.site.register(ExperienceModel)
admin.site.register(SkillModel)
admin.site.register(EducationModel)
admin.site.register(ProjectCategoryModel)
