from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


from django.contrib.auth import authenticate, login

# Create your views here.



def login(request):

	if request.method == "POST":
		username = request.POST['email']
		password = request.POST['password']

		user = auth.authenticate(username=username,password=password)

		if user:
			auth.login(request, user)
			return redirect('/')

		else:
		    messages.info(request,'invalid credentials')
		    return render(request,'travels_app/login.html')	

	else:
	    return render(request,'travels_app/login.html')



def register(request):

	if request.method == "POST":
		first_name = request.POST.get('first_name')
		last_name  = request.POST.get('last_name')
		username   = request.POST.get('username')
		email      = request.POST.get('email')
		phoneno    = request.POST.get('phoneno')
		address    = request.POST.get('address')
		password1  = request.POST.get('password1')
		password2  = request.POST.get('password2')

		
		if password1==password2:

			if User.objects.filter(email=email).exists():
				messages.info(request,'Email Taken')
				return redirect('register')

			else:	
				user = User.objects.create_user(username=email, password=password1, email=email, first_name=first_name, last_name=last_name)
				user.save()
				print("user created")
				return redirect('login')


		else:
		    messages.info(request,'Password did not match')
		    return redirect('register')


		return redirect('/')

	else:
		return render(request,'travels_app/register.html')



def logout(request):
	auth.logout(request)
	return redirect('/')

		


	