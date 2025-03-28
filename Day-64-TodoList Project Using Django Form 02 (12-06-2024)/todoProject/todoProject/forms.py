from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from todoApp.models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUserModel
        fields=UserCreationForm.Meta.fields+('city','profile_pic','user_type','email','first_name','last_name')

    def clean_user_type(self):
        user_type = self.cleaned_data.get('user_type')
        if user_type == 'admin' and CustomUserModel.objects.filter(user_type='admin').exists():
            raise forms.ValidationError("An admin user already exists.")
        return user_type
            
class CustomUserAuthenticationForm(AuthenticationForm):
    class Meta:
        model=CustomUserModel
        fields=['username','password']
        
class CustomCategoryForm(forms.ModelForm):
    class Meta:
        model=CategoryModel
        fields=['category_name']

class CustomTaskForm(forms.ModelForm):
    class Meta:
        model=TaskModel
        fields=['task_name','category','task_description','task_status','task_priority','due_date','completed_date']
        
        widgets={
            'due_date':forms.DateInput(attrs={'type':'date', 'class':'date-field'}),
            'completed_date':forms.DateInput(attrs={'type':'date','class':'date-field'}),
            'task_description':forms.Textarea(attrs={'type':'text','class':'textarea-field'}),
            'task_status':forms.TextInput(attrs={
                'readonly':'readonly',
            })
        }
        
        labels={
            "task_description":"Enter description",
       }