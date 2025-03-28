from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from signInUpApp.models import *

class CustomUserForm(UserCreationForm):
    class Meta:
        model=CustomUserModel
        fields=UserCreationForm.Meta.fields+('first_name','last_name','email','City','Profile_Picture','User_Type')

class CustomAuthForm(AuthenticationForm):
    class Meta:
        model=CustomUserModel
        fields=['username','password']