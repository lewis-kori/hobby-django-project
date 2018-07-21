from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django import forms

class EditProfileForm(UserChangeForm):
    
    class Meta:
        model =User
        fields=('first_name','last_name','email','password')