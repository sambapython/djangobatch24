from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from product.models import Category, Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "cost", "deliver_charges", "category","id"]

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["name","discount"]

    def validate_name(self, value):
        # write name validartion code
        return value

class CategoryGetSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["name","discount","id","hide"]
