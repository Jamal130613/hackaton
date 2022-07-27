from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.product.views import CategoryView

from applications.product.views import ProductView

router = DefaultRouter()
router.register('category', CategoryView)
router.register('',ProductView)




urlpatterns = [
    path('', include(router.urls))
]

