from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250)
    hide = models.BooleanField(default=False)
    discount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return  "%s-%s" %(self.name, self.discount)

class Product(models.Model):
    name = models.CharField(max_length=250)
    cost = models.PositiveIntegerField(default=0)
    deliver_charges = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    #many to one
    #category = models.CharField(max_length=250)
    # in this column we can add only category table id column values only

class Customer(models.Model):
    name = models.CharField(max_length=250)
    # address = models.Textfield(max_length=650)
    # phone = models.CharField(max_length=11)
    # email = models.CharField(max_length=250)

class Sales(models.Model):
    description = models.CharField(max_length=250)
    products = models.ManyToManyField(Product, through='SalesProducts')
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class SalesProducts(models.Model):
    sales = models.ForeignKey(Sales, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    cost = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=1)



    

