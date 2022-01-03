from django.core.files.base import equals_lf
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from product.models import Category, Product, Sales, Customer
from django.contrib.auth.decorators import login_required
from product.forms import CategoryForm, product_form_set, SalesForm, ProductForm
from django.contrib import messages
from django.core.cache import cache
def view_product_create(request):
    if request.method=="POST":
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(message="Product created successfully", request=request)
            return redirect("/products/")
        else:
            messages.error(message=form._errors, request=request)
    else:
        form = ProductForm()
    context = {"form": form}
    return render(request, "product_create.html", context)

def view_sales_create(request):
    context = {"customers": Customer.objects.all()}
    if request.method == "POST":
        sale_form = SalesForm(data=request.POST)
        total_product_forms = int(request.POST.get("form-TOTAL_FORMS"))
        initial_data = [{"cost":request.POST.get("form-%s-cost"%i),
                        "product":request.POST.get("form-%s-product"%i),
                        "quantity":request.POST.get("form-%s-quantity"%i),
                        } for i  in  range(total_product_forms)]
        product_forms = product_form_set(initial = initial_data)
        if "submit" in request.POST:
            if sale_form.is_valid():
                sale_form.instance.save()
                sale_id = sale_form.instance.id
                product_forms = product_form_set(request.POST)
                for product_form in  product_forms.forms:
                    if product_form.is_valid():
                        product_form.instance.sales_id=sale_id
                        product_form.instance.save()
                    else:
                        messages.error(messages=product_form._errors, request=request)
                messages.success(message="Sales Order submitted Successfully!",
                                    request=request)
                return redirect("/sales/")
            else:
                errors = []
                if sale_form._errors:
                    errors.append( sale_form._errors)
                # if product_forms._errors:
                #     errors.append(product_forms._errors)
                messages.error(message=errors, request=request)    
    else:
        sale_form = SalesForm()
        product_forms = product_form_set()
    context = {"sale_form":sale_form, "product_forms": product_forms}
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
            cache.delete("customers")
        return redirect("/customers/")
    context = {"data": cust_inst}
    return render(request, "confirm_customer.html", context)
    
    

def view_update_customer(request, cust_id):
    cust_inst = Customer.objects.get(id=cust_id)
    if request.method == "POST":
        cust_inst.name=request.POST.get("name")
        cust_inst.save()
        cache.delete("customers")
        return redirect("/customers/")
        #return view_categories(request)

    context = {"data": cust_inst}
    return render(request, "create_customer.html", context)
def view_create_customer(request):
    if request.method == "POST":
        data = request.POST
        cust_inst = Customer(name=data.get("name"))
        raise Exception("dsdfsdf")
        cust_inst.save()
        cust_inst.save(using="backup")
        cache.delete("customers")
        # context = {"cats": Customer.objects.all()}
        # return render(request, 'categories.html',context)
        return redirect("/customers/")
    return render(request, 'create_customer.html')

def view_customers(request):
    cache_data = cache.get("customers")
    if cache_data:
        data = cache_data
    else:
        data = Customer.objects.all()
        cache.set("customers",data)
    context = {"cats": data}

    return render(request, 'customers.html',context)




def view_hide_category(request, cat_id):
    cat_inst = Category.objects.get(id=cat_id)
    if request.method == "POST":
        if 'delete' in request.POST:
            cat_inst.hide=True
            cat_inst.save()
        return redirect("/categories/")
    context = {"data": cat_inst}# {"object": cat_inst}
    return render(request, "confirm.html", context)
