from django.http.response import HttpResponse
from emp.views import get_employees, create_emp
from django.urls import path
from django.http import HttpResponse
app_name = "emp"
def fun(request):
    return HttpResponse("from urls")
urlpatterns = [
    path("", get_employees),
    #path("createEmp/", fun, name="create1_emp"),#emp/createEmp/
    path("createEmp/", create_emp, name="create_emp"),
    path("updateEmp/", create_emp, name="create_emp"),
    
]