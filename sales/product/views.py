from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from product.models import Category, Product, Sales, Customer
from django.contrib.auth.decorators import login_required
def view_sales_create(request):
    context = {"customers": Customer.objects.all()}
    if request.method == "POST":
        context = {"products": Product.objects.all(),"sales_data":request.POST}
        return render(request, "add_product.html", context)
    return render(request, "create_sales.html", context)

@login_required
def view_sales(request):
    contrext = {"data":Sales.objects.all()}
    return render(request, 'sales.html', contrext)
    

def view_products(request):
    context = {"data": Product.objects.all()}
    return render(request, "products.html", context)

def view_index(request):
    return render(request, "base.html")

# Create your views here.
def view_delete_customer(request, cust_id):
    cust_inst = Customer.objects.get(id=cust_id)
    if request.method == "POST":
        if "delete" in request.POST:
            cust_inst.delete()
        return redirect("/customers/")
    context = {"data": cust_inst}
    return render(request, "confirm_customer.html", context)
    
    

def view_update_customer(request, cust_id):
    cust_inst = Customer.objects.get(id=cust_id)
    if request.method == "POST":
        cust_inst.name=request.POST.get("name")
        cust_inst.save()
        return redirect("/customers/")
        #return view_categories(request)

    context = {"data": cust_inst}
    return render(request, "create_customer.html", context)
def view_create_customer(request):
    if request.method == "POST":
        data = request.POST
        cust_inst = Customer(name=data.get("name"))
        cust_inst.save()
        # context = {"cats": Customer.objects.all()}
        # return render(request, 'categories.html',context)
        return redirect("/customers/")
    return render(request, 'create_customer.html')

def view_customers(request):
    # need to get the the stored categories and send as a resposne.
    #return HttpResponse("cats")
    #return HttpResponse(data)
    #context = {"cats": Customer.objects.all()}
    context = {"cats": Customer.objects.all()}
    return render(request, 'customers.html',context)




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


