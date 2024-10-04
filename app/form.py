from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import RegisterUser

class RegisterUserForm(UserCreationForm):
    email_address = forms.EmailField(required=True)

    class Meta:
        model = RegisterUser
        fields = ("first_name", 'last_name', 'username', 'email_address', 'password1','password2')

    
    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email_address']
        if commit:
            user.save()
        return user
    


class LoginUser(AuthenticationForm):
    username = forms.CharField(max_length=250, required=True, label='username'),
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='password')