from rest_framework import serializers
from applications.product.models import Category, Image
from applications.product.models import Product
from applications.product.models import Review


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

class ReviewSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Review
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.email')
    reviews = ReviewSerializer(many=True,read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        product = Product.objects.create(**validated_data)

        return product

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes'] = instance.likes.filter(like=True).count()
        return representation



class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


