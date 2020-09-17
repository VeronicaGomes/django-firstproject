from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Account

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=50)

	class Meta:
		model = Account
		fields = ('email', 'username', 'first_name', 'last_name', 'number', 'addr', 'password1', 'password2')