from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
	    model = User
	    fields = ["username", "email", "password1", "password2"]

class EditProfileForm(forms.ModelForm):
     class Meta:
         model=User
         fields = ('first_name','last_name',)
