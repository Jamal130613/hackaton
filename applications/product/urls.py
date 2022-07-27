from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.product.views import CategoryView

from applications.product.views import ProductView

from applications.product.views import ReviewView

router = DefaultRouter()
router.register('category', CategoryView)
router.register('comment', ReviewView)
router.register('',ProductView)




urlpatterns = [
    path('', include(router.urls))
]

