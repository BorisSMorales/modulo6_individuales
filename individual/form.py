from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioRegistro(forms.Form):
    usuario = forms.CharField(label="Usuario", max_length=50, required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre de Usuario', 'class': 'form-control'}),
                            error_messages={'required':'El nombre es obligatorio', 'max_length': 'el nombre no puede tener más de 50 caracteres'})
    email = forms.EmailField(label="Email", max_length=100,min_length=5, required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Ingrese su Email', 'class': 'form-control'}),
                            error_messages={'required':'El Email es obligatorio', 'max_length':'el email no puede tener más de 100 caracteres','min_length': 'El email debe tener al menos 5 caracteres'})
    nombre = forms.CharField(label='Nombre', max_length=100, required=True,
                            widget=forms.TextInput(attrs={'placeholder':'Ingrese su nombre ', 'class':'form-control'}),
                            error_messages= {'required':'Nombre es obligatorio', 'max_lenght':'Su nombre es muy largo :c'})
    apellido = forms.CharField(label='Apellido', max_length=100, required=True,
                            widget=forms.TextInput(attrs={'placeholder':'Ingrese su apellido', 'class':'form-control'}),
                            error_messages= {'required':'El asunto es obligatorio', 'max_lenght':'El asunto no debe tener mas de 100 caracteres'})
    
class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', required=True,
                            max_length=50, min_length=5,
                            error_messages={
                                'required': 'El usuario es obligatorio',
                                'max_length': 'El usuario no puede superar los 50 caracteres',
                                'min_length': 'El usuario debe tener al menos 5 caracteres'
                            },
                            widget=forms.TextInput(attrs={
                                'placeholder': 'Ingrese su usuario',
                                'class': 'form-control'
                            })
                            )
    password = forms.CharField(label='Contraseña', required=True,
                            max_length=50, min_length=1,
                            error_messages={
                                'required': 'La contraseña es obligatoria',
                                'max_length': 'La contraseña no puede superar los 50 caracteres',
                                'min_length': 'La contraseña debe tener al menos 1 caracter'
                            },
                            widget=forms.PasswordInput(attrs={
                                'placeholder': 'Ingrese su contraseña',
                                'class': 'form-control'
                            })
                            )
    
class RegistroForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')