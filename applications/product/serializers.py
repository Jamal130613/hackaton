from rest_framework import serializers

from applications.product.models import Category

from applications.product.models import Product

from applications.product.models import Comment

from applications.product.models import Image


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print(representation)
        if not instance.parent:
            representation.pop('parent')
        return representation


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Comment
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    images = ImageSerializer(many=True, read_only=True)
    отзывы = CommentSerializer(many=True,read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        requests = self.context.get('request')
        images = requests.FILES
        product = Product.objects.create(**validated_data)
        print(images)

        for image in images.getlist('images'):
            Image.objects.create(product=product, image=image)

        return product

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes'] = instance.likes.filter(like=True).count()
        return representation



