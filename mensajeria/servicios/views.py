from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import servicio

from .models import servicio

# Create your views here.

def holaMundo(request):
    return HttpResponse("Hola Mundo ADSO")

def inicio(request):
    return render(request, 'inicio.html')

def lista_servicios(request):
    servicios_list = servicio.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios_list})
def detalle(request,servicios_id):
    servicios = get_object_or_404(servicio, id=servicios_id)
    return render(request, 'detalle.html',{'servicio':servicio})
