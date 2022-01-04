from rest_framework.serializers import ModelSerializer
from product.models import Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["name","discount"]

class CategoryGetSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["name","discount","id","hide"]
