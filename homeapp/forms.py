from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from homeapp.models import Register,Personhomepage


class registerForm(ModelForm):
     class Meta:
         model = Register
         exclude=['user']
         


class EditForm(forms.ModelForm):
                             
    class Meta:
        model = User
        fields = ['username', 'email' ,'first_name','last_name']
        
class personhomepageFrom(ModelForm):
    class Meta:
        model = Personhomepage
        exclude=['user']