from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from todoApp.models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUserModel
        fields=UserCreationForm.Meta.fields+('city','profile_pic','user_type','email','first_name','last_name')
        
class CustomUserAuthenticationForm(AuthenticationForm):
    class Meta:
        model=CustomUserModel
        fields=['username','password']