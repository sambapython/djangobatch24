from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, logout
from django.contrib.auth.models import User
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
		username = request.POST.get("username")
		password = request.POST.get("password")
		try:
			User.objects.create_user(username=username, password=password)
			message="user created successfully"
		except Exception as err:
			#message=err
			message = "Username already exist!! SignUp failed!!"
	context = {"message":message}
	return render(request, "signup.html", context)

def view_signout(request):
	logout(request)
	return redirect("/")