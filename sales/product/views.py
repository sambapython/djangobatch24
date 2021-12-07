from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from product.models import Category

# Create your views here.
def view_create_category(request):
    if request.method == "POST":
        data = request.POST
        cat_inst = Category(name=data.get("name"))
        cat_inst.save()
        # context = {"cats": Category.objects.all()}
        # return render(request, 'categories.html',context)
        return redirect("/categories/")
    return render(request, 'create_category.html')

def view_categories(request):
    # need to get the the stored categories and send as a resposne.
    #return HttpResponse("cats")
    #return HttpResponse(data)
    context = {"cats": Category.objects.all()}
    return render(request, 'categories.html',context)


