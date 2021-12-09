from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from product.models import Category

def view_index(request):
    return render(request, "base.html")

def view_hide_category(request, cat_id):
    cat_inst = Category.objects.get(id=cat_id)
    if request.method == "POST":
        if 'delete' in request.POST:
            cat_inst.hide=True
            cat_inst.save()
        return redirect("/categories/")
    context = {"data": cat_inst}
    return render(request, "confirm.html", context)

# Create your views here.
def view_delete_category(request, cat_id):
    cat_inst = Category.objects.get(id=cat_id)
    if request.method == "POST":
        if "delete" in request.POST:
            cat_inst.delete()
        return redirect("/categories/")
    context = {"data": cat_inst}
    return render(request, "confirm.html", context)
    
    

def view_update_category(request, cat_id):
    cat_inst = Category.objects.get(id=cat_id)
    if request.method == "POST":
        cat_inst.name=request.POST.get("name")
        cat_inst.save()
        return redirect("/categories/")
        #return view_categories(request)

    context = {"data": cat_inst}
    return render(request, "create_category.html", context)
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
    #context = {"cats": Category.objects.all()}
    context = {"cats": Category.objects.filter(hide=False)}
    return render(request, 'categories.html',context)


