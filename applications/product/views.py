from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from applications.product.models import Category
from applications.product.permissions import CustomIsAdmin
from applications.product.serializers import CategorySerializer
from applications.product.models import Product
from applications.product.serializers import ProductSerializer
from applications.product.models import Like
from applications.product.models import Review
from applications.product.serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomIsAdmin]


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['name', 'description']
    ordering_fields = ['price']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(methods=['POST'], detail=True)
    def like(self,request, pk, *args, **kwargs):
     try:

        like_object, _ =  Like.objects.get_or_create(owner=request.user,product_id=pk)
        like_object.like = not like_object.like
        like_object.save()
        status = 'liked'

        if like_object.like:
            return Response({'status': status})
        status = 'unliked'
        return Response({'status': status})
     except:
         return Response('Такого продукта не существует!')
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        elif self.action == 'like':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthenticated]

        return [p() for p in permissions]


class ReviewView(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
