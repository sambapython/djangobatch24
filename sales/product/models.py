from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250)
    hide = models.BooleanField(default=False)

    def __str__(self):
        return  self.name
