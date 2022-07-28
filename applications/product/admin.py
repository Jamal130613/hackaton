from django.contrib import admin
from applications.product.models import Category, Image
from applications.product.models import Product
from applications.product.models import Like
from applications.product.models import Review

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Like)
admin.site.register(Review)
admin.site.register(Image)