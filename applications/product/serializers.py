from rest_framework import serializers

from applications.product.models import Category

from applications.product.models import Product


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

class ProductSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        product = Product.objects.create(**validated_data)

        return product

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation