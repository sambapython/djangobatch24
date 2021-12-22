from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, logout
from product.forms import MyUserForm
from django.contrib import messages
def view_signin(request):
	message=""
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(username=username, password=password)
		if user:
			message = "User loged in successfully!!" 
			login(request, user)
			next_url = request.GET.get("next","/")
			return redirect(next_url)
		else:
			message = "User not loged in, Wrong credentials!!"

	context = {"message":message}
	return render(request, "signin.html", context)

def view_signup(request):
	message=""
	if request.method == "POST":
		form = MyUserForm(data=request.POST)
		if form.is_valid():
			form.instance.save()
			myuser = form.instance
			user = myuser.user_ptr
			user.set_password(request.POST.get("password"))
			user.save()
			messages.success(request=request, message="User created successfully")
		else:
			messages.error(request=request, message=form._errors)
	else:
		form = MyUserForm()
	context = {"message":message, "form": form}
	return render(request, "signup.html", context)

def view_signout(request):
	logout(request)
	return redirect("/")