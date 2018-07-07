from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
        labels = {
            'username':'nombre de usuario',
            'first_name':'Nombre',
            'last_name':'Apellidos',
            'email': 'Correo Electronico',
            'password':'Contraseña'}

        exclude=[]
        widgets = {
            'username':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre usuario'}),
            'first_name':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre'}),
            'last_name': forms.DateInput(attrs={'class': 'form-control', 'placeholder':'Apellidos'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'contraseña'})
        }


