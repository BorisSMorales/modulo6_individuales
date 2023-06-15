from django import forms 

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
    
