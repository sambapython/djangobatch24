from django.db import models
from product.validations import validate_name
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class BaseAbstarctModel(models.Model):# Abstract model
    name=models.CharField(max_length=250, validators=[validate_name])
    created_at = models.DateTimeField(default=datetime.now())
    class Meta:
        abstract=True

# class MyUser(User): # inherited model
#     #it will create myuser table in db after migrate.
#     # we have inherited this model from user, i.e it will create a one to one relationship
#     # with User model
#     phone = models.CharField(max_length=250, default="", null=True)
#     adhar = models.CharField(max_length=250, default="", null=True)
#     pan = models.CharField(max_length=250, default="", null=True)
#     passport = models.CharField(max_length=250, default="", null=True)

class MyUser(AbstractUser):
    phone = models.CharField(max_length=250, default="", null=True)
    adhar = models.CharField(max_length=250, default="", null=True)
    pan = models.CharField(max_length=250, default="", null=True)
    passport = models.CharField(max_length=250, default="", null=True)

# Create your models here.
class Category(BaseAbstarctModel):
    #name=models.CharField(max_length=250, validators=[validate_name])
    hide = models.BooleanField(default=False)
    discount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return  "%s-%s" %(self.name, self.discount)

class Product(BaseAbstarctModel):
    #name = models.CharField(max_length=250)
    cost = models.PositiveIntegerField(default=0)
    deliver_charges = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.FileField(default="")
    #many to one
    #category = models.CharField(max_length=250)
    # in this column we can add only category table id column values only

    def __str__(self):
        return self.name

class Customer(BaseAbstarctModel):
    pass
    #name = models.CharField(max_length=250)
    # address = models.Textfield(max_length=650)
    # phone = models.CharField(max_length=11)
    # email = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Sales(models.Model):
    description = models.CharField(max_length=250)
    products = models.ManyToManyField(Product, through='SalesProducts')
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class SalesProducts(models.Model):
    sales = models.ForeignKey(Sales, on_delete=models.PROTECT)
    #product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    cost = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=1)



    

