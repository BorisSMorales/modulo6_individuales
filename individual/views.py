from django.shortcuts import render
import uuid

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView, FormView
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from individual.form import FormularioRegistro, LoginForm
from individual.models import Registromodel
# Create your views here.

def landing(request):
    return render(request, 'landingpage.html')





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
    

class Ingreso(TemplateView):
    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, self.template_name, { "form": form })

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('landing')
            form.add_error('username', 'Credenciales incorrectas')
            return render(request, self.template_name, { "form": form })
        else:
            return render(request, self.template_name, { "form": form })
        
class UsuariosRestringidaView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'usuarios.html'
    permission_required = 'individual.puede_ver_usuarios'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = User.objects.exclude(is_superuser=True)
        context['users'] = users
        return context

    def get(self, request, *args, **kwargs):
        titulo = "Restringido"
        if titulo is None:
            return redirect('landing')
        return super().get(request, *args, **kwargs)
    

class AreaRestringidaView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'restringido.html'
    permission_required = 'individual.puede_ver_pagina'
    def get(self, request, *args, **kwargs):
        titulo = "Restringido"
        contexto = {
        'titulo': titulo,
        }
        if titulo is None:
            return redirect('landing')
        return render(request, self.template_name, contexto)