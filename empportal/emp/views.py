from django.shortcuts import render
#from django.http import HttpResponse

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

