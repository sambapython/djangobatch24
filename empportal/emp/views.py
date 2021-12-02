from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from emp.models import Emp
#from django.http import HttpResponse

def create_emp(request):
    return HttpResponse("hello")
def get_employees(request):
    emps = Emp.objects.all()
    #emps is the list of Emp class(django model) instances. 
    #return HttpResponse(emps)
    # Above return statement will throw an error. Django server not able to understand the 
    # django model instances.
    #serialization. we need to convert list of django model instances to list of dictionaires.
    #data = [{"name":emp.name,"salary":emp.salary_perday} for emp in emps]

    #return HttpResponse(data)
    return render(request, "emp/emps.html", {"emps": emps})

# Create your views here.
def home(request):
    # resp = """
    # <html>
    # <body>
    # <h1>HOME</h1>
    # </body>
    # </html>
    # """
    #return HttpResponse("HOME")
    #1. we need to write this html content in html file
    #2. read the html content from html file 
    #3. prepare HttpREsponse object
    #2,3 will be done by render function 
    # home.html
    #return HttpResponse(resp)
    employees = [{"name":"Hameer"},{"name":"Anil"},{"name":"Vamshi"}]
    data = {"title":"Empportal", "header":"PORTAL"}
    context = {"data": data, "employees": employees}
    return render(request, "home.html", context)
    # render has to serach for home.html

