from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
def view_signin(request):
	message=""
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		if authenticate(username=username, password=password):
			message = "User loged in successfully!!" 
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