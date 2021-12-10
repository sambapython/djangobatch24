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
    #category = models.CharField(max_length=250)
    # in this column we can add only category table id column values only

class Sales(models.Model):
    pass

