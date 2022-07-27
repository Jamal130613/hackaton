from rest_framework.viewsets import ModelViewSet

from applications.product.models import Category
from applications.product.serializers import CategorySerializer

from applications.product.models import Product
from applications.product.serializers import ProductSerializer


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer