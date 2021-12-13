"""sales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from product.views import view_categories, view_create_category, view_update_category,\
    view_delete_category, view_hide_category, view_index, view_products, view_sales,\
    view_sales_create, view_customers, view_create_customer, view_update_customer,\
    view_delete_customer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', view_categories),# view_categories(request_obj)
    path('category/create/', view_create_category),
    path('category/update/<int:cat_id>/', view_update_category),
    #view_update_category(request_obj, cat_id=5)
    path('category/delete/<int:cat_id>/', view_delete_category),
    #view_delete_category(request_obj, cat_id=1)
    path('category/hide/<int:cat_id>/', view_hide_category),
    path('customers/', view_customers),# view_categories(request_obj)
    path('customer/create/', view_create_customer),
    path('customer/update/<int:cust_id>/', view_update_customer),
    #view_update_customer(request_obj, cat_id=5)
    path('customer/delete/<int:cust_id>/', view_delete_customer),
    #view_delete_customer(request_obj, cat_id=1)
    # path('customer/hide/<int:cust_id>/', view_hide_customer),
    path("", view_index),
    path("products/", view_products),
    path("sales/", view_sales),
    path("sales/create/", view_sales_create)
]
