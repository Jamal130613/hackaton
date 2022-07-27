from django.contrib import admin

from applications.product.models import Category

from applications.product.models import Product

admin.site.register(Category)
admin.site.register(Product)
