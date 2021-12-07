from django.http.response import HttpResponse
from emp.views import get_employees, create_emp, update_emp,\
    delete_emp
from django.urls import path
from django.http import HttpResponse
app_name = "emp"
def fun(request):
    return HttpResponse("from urls")
urlpatterns = [
    path("", get_employees),
    #path("createEmp/", fun, name="create1_emp"),#emp/createEmp/
    path("createEmp/", create_emp, name="create_emp"),
    path("updateEmp/<int:emp_id>/", update_emp, name="updateEmp"),
    path("deleteEmp/<int:emp_id>/", delete_emp, name="deleteEmp"),
    #http://localhost:8000/emp/updateEmp/7/
    # update_emp(request_obj, emp_id=7)
    
]