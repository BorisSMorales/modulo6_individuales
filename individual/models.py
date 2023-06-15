from django.db import models

# Create your models here.

class Registromodel(models.Model):
    usuario = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    apellido = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nombre
    
    class Meta:
            permissions = [
                ('puede_ver_usuarios', 'Permiso para ver usuarios')
            ]