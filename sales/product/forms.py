from django.db import models
from django.db.models import fields
from django.forms import ModelForm, formset_factory
from product.models import Category, Product, Sales, SalesProducts
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class MyUserForm(ModelForm):
    class Meta:
        model=get_user_model()# returns the MyUser model class
        fields=["username", "password","first_name","last_name","phone","pan","adhar","passport"] #"__all__"


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__" #["name","discount"]
        exclude = ["hide", "created_at"]

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ["hide","created_at"]

    # def clean(self):
    #     # this get called when you call form.is_valid method
    #     if not self.data.get("name").isalnum():
    #         raise ValidationError("Name expecting only numbers and alphabets")
    #     if self.data.get("discount")<0:
    #         raise ValidationError("Expecting discount>0")
    #     return super(CategoryForm, self).clean()

class SalesForm(ModelForm):
    class Meta:
        model = Sales
        fields = "__all__"
        exclude = ["products"]

class SalesProductsForm(ModelForm):
    class Meta:
        model = SalesProducts
        fields = "__all__"
        exclude = ["sales"]
product_form_set = formset_factory(SalesProductsForm, extra=1)

