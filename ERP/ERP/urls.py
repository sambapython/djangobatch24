"""ERP URL Configuration

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
from accounting import views as accounting_views
from sales import views as sales_views 
from stock import views as stock_views 
from pur import views as purchase_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounting/index/", accounting_views.index),
    path("sales/index/", sales_views.index),
    path("pur/index/", purchase_views.index),
    path("stock/index/", stock_views.index),

]
