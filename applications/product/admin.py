from django.contrib import admin
from applications.product.models import Category, Like, Product, Review, Image

admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Review)
admin.site.register(Image)


class ImageInAdmin(admin.TabularInline):
    model = Image
    fields = ['image']
    max_num = 5


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    search_fields = ['price', 'name']

admin.site.register(Product, ProductAdmin)
