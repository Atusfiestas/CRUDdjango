from django.shortcuts import render, HttpResponse

# Create your views here.

def holaMundo(request):
    return HttpResponse("Hola Mundo ADSO")

def inicio(request):
    return render(request, 'inicio.html')
