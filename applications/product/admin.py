from django.contrib import admin

from applications.product.models import Category

from applications.product.models import Product

from applications.product.models import Like

from applications.product.models import Comment

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Like)
admin.site.register(Comment)