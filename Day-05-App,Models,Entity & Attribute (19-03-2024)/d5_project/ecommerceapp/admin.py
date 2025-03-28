from django.contrib import admin
from ecommerceapp.models import ProductModel,OrderModel,ReviewModel,SellerModel,PaymentModel

# Register your models here.

admin.site.register(ProductModel)
admin.site.register(OrderModel)
admin.site.register(ReviewModel)
admin.site.register(SellerModel)
admin.site.register(PaymentModel)