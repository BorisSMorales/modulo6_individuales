from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def landing(request):
    return render(request, 'landingpage.html')



def user_list(request):
    users = User.objects.exclude(is_superuser=True)
    return render(request, 'usuarios.html', {'users': users})