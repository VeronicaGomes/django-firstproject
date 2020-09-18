from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from accounts.forms import RegistrationForm
from django.contrib.auth import authenticate, login

# Create your views here.

def register(request):

	context = {}
	if request.POST:
		
		form = RegistrationForm(request.POST)

		if form.is_valid():

			user = form.save()

			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')

			# accounts = authenticate(email=email, password=raw_password)
			# login(request, accounts)
			
			return redirect('/')

		else:

			context['registration_form'] = form	

	else:

		form = RegistrationForm()
		context['registration_form'] = form
		
	return render(request, 'travels_app/register.html', context)    	    


	




	