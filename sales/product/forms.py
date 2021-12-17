from django.forms import ModelForm  
from product.models import Category
from django.core.exceptions import ValidationError

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__" #["name","discount"]
        exclude = ["hide"]

    # def clean(self):
    #     # this get called when you call form.is_valid method
    #     if not self.data.get("name").isalnum():
    #         raise ValidationError("Name expecting only numbers and alphabets")
    #     if self.data.get("discount")<0:
    #         raise ValidationError("Expecting discount>0")
    #     return super(CategoryForm, self).clean()


