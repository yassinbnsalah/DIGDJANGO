from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, widgets
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username','email','password1' ,'password2'] 
        
        widget = {
            'username' : widgets.TextInput(attrs = {'class' : 'form-control'}),
            'email' :  widgets.TextInput(attrs = {'class' : 'form-control'}),
            'password1' :  widgets.TextInput(attrs = {'class' : 'form-control'}) 
        } 