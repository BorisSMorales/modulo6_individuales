from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView, FormView
from django.views import View

from individual.form import FormularioRegistro
from individual.models import Registromodel
# Create your views here.

def landing(request):
    return render(request, 'landingpage.html')



def user_list(request):
    users = User.objects.exclude(is_superuser=True)
    return render(request, 'usuarios.html', {'users': users})

class FormularioRegistroView(TemplateView):
    template_name = 'formregistro.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formulario'] = FormularioRegistro()  # Sin inicializar el formulario
        return context

    def post(self, request, *args, **kwargs):
        form = FormularioRegistro(request.POST)
        mensajes = {
            "enviado": False,
            "resultado": None
        }
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            email = form.cleaned_data['email']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']

            registro = Registromodel(
                usuario=usuario,
                email=email,
                nombre=nombre,
                apellido=apellido,
            )
            registro.save()

            mensajes = { "enviado": True, "resultado": "Usuario registrado en formulario" }
        else:
            mensajes = { "enviado": False, "resultado": form.errors }
        return render(request, self.template_name, { "formulario": form, "mensajes": mensajes })