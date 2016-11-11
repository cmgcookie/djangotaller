from django.shortcuts import render
from django.http import HttpResponse


def hola(request):
    return render(request, "index.html", {"nombre":"Cookie Monster"})
    #return HttpResponse("Hello World from Django")

def formulario(request):
    form = "Hola aquí el formulario"
    return render(request, "formulario.html", {"formulario":form})
# Create your views here.
