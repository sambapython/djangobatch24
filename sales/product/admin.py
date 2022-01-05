from django.contrib import admin
from product.models import Category, MyUser
#from rest_framework.authtoken.models import Token

# Register your models here.
admin.site.register(Category)
admin.site.register(MyUser)
#admin.site.register(Token)
