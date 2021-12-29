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
from django.contrib.messages.api import success
from django.urls import path
from product.models import Category
from product.views import view_categories,view_hide_category, view_products, view_sales,\
    view_sales_create, view_customers, view_create_customer, view_update_customer,\
    view_delete_customer, view_product_create

from product import user_auth
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView, CreateView, UpdateView,\
    DeleteView, ListView
from product.forms import CategoryForm

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('categories/', view_categories),# view_categories(request_obj)
    path('categories/', ListView.as_view(
        model = Category,
        template_name="categories.html",
        paginate_by=10
    )),# view_categories(request_obj)
    #path('category/create/', view_create_category),
    path('category/create/', CreateView.as_view(
        model = Category,
        fields = ["name","discount"],
        #exclude = ["hide", "created_at"],
        #form_class = CategoryForm,
        success_url = "/categories/",
        template_name="create_category.html"
        # default template: category_form.html
    )),
    #path('category/update/<int:cat_id>/', view_update_category),
    path('category/update/<int:pk>/', UpdateView.as_view(
        model = Category,
        fields = ["name","discount"],
        #exclude = ["hide", "created_at"],
        #form_class = CategoryForm,
        success_url = "/categories/",
        template_name="create_category.html"
        # default template: category_form.html 
    )),
    #view_update_category(request_obj, cat_id=5)
    #path('category/delete/<int:cat_id>/', view_delete_category),
    path('category/delete/<int:pk>/', DeleteView.as_view(
        model=Category,
        success_url = "/categories/",
        template_name="confirm.html",
    )),
    #view_delete_category(request_obj, cat_id=1)
    path('category/hide/<int:cat_id>/', view_hide_category),
    path('customers/', view_customers),# view_categories(request_obj)
    path('customer/create/', view_create_customer),
    path('customer/update/<int:cust_id>/', view_update_customer),
    #view_update_customer(request_obj, cat_id=5)
    path('customer/delete/<int:cust_id>/', view_delete_customer),
    #view_delete_customer(request_obj, cat_id=1)
    # path('customer/hide/<int:cust_id>/', view_hide_customer),
    #path("", view_index),
    path("", TemplateView.as_view(
        template_name="base.html",
        )),
    path("products/", view_products),
    path("sales/", view_sales),
    path("sales/create/", view_sales_create),
    path("signin/",user_auth.view_signin),
    path("signup/",user_auth.view_signup),
    path("signout/", user_auth.view_signout),
    path("product/create/", view_product_create)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
