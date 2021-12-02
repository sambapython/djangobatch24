from emp.views import get_employees, create_emp
from django.urls import path
urlpatterns = [
    path("", get_employees),
    path("createEmp1234/", create_emp, name="create_emp"),
    
]