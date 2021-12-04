from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from emp.models import Emp
#from django.http import HttpResponse

def update_emp(request, emp_id):
    emp_ins = Emp.objects.get(id=emp_id)
    if request.method=="POST":
        new_data = request.POST
        emp_ins.name =  new_data.get("name")
        emp_ins.empid = new_data.get("empid")
        emp_ins.salary_perday = new_data.get("salary_perday")
        emp_ins.email = new_data.get("email")
        emp_ins.phone = new_data.get("phone")
        emp_ins.address = new_data.get("address")
        emp_ins.emp_type = new_data.get("emp_type")
        emp_ins.save()
        return redirect('/emp/')
        # emps = Emp.objects.all() 
        # return render(request, "emp/emps.html", {"emps": emps})

    return render(request, 'emp/create.html', {"data":emp_ins})
    import pdb;pdb.set_trace()



def create_emp(request):
    #return HttpResponse("hello")
    print("*"*20)
    print(request.method)
    if request.method == "POST":
        act_data = request.POST
        data = {"name": act_data.get("name"),
        "empid": act_data.get("empid"),
        "salary_perday": act_data.get("salary_perday"),
        "email": act_data.get("email"),
        "phone": act_data.get("phone"),
        "address": act_data.get("address"),
        "emp_type": act_data.get("emp_type"),
        }
        emp_inst = Emp(**data)
        emp_inst.save()
        return redirect('/emp/')
        # emps = Emp.objects.all() 
        # return render(request, "emp/emps.html", {"emps": emps})

    type_choices = Emp.emp_type_choices
    return render(request, "emp/create.html", {"emp_types": type_choices})

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

