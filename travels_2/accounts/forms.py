from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Account

class RegistrationForm(UserCreationForm):

	class Meta:
		model = Account
		fields = ('email', 'first_name', 'last_name', 'number', 'addr', 'password1', 'password2')
