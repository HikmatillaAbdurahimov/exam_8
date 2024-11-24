from .models import Products,Categories
from rest_framework import serializers

class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model=Categories
        fields=['id','title','image','create_at','description']


class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=['id','title','image','create_at','description']