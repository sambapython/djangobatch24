from emp.views import get_employees
from django.urls import path
urlpatterns = [
    path("", get_employees),
    path("createemp", get_employees),
    
]