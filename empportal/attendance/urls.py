
from django.urls import path
from django.http import HttpResponse
def fun(request):
    return HttpResponse("hello")

app_name = "attendance"
urlpatterns = [
    path("attendance_create_emp/", fun, name="create_emp"),
    
]