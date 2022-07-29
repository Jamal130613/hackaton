from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.product.views import CategoryView

from applications.product.views import ProductView

from applications.product.views import ReviewView

from applications.product.models import Image

router = DefaultRouter()
router.register('category', CategoryView)
router.register('review', ReviewView)
router.register('',ProductView)


class ImageInAdmin(admin.TabularInline):
    model = Image
    fields = ['image']
    max_num = 5


urlpatterns = [
    path('', include(router.urls))
]

