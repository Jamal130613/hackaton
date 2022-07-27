from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    pass


class Image(models.Model):
    image = models.ImageField(upload_to='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='images')