from django.shortcuts import render
from django.http import HttpResponse
from .forms import infoGeneralForm
from .models import infoGeneral

def hola(request):
    return render(request, "index.html", {"nombre":"Cookie Monster"})
    #return HttpResponse("Hello World from Django")

def formulario(request):
    #form = "Hola aquí el formulario"
    form = infoGeneralForm()
    if request.method=="post":
        form=infoGeneralForm(request.post)
        if form.is_valid():
            form.save()
            return render(request, "formulario.html", {"formulario":"Gracias, datos guardados exitosamente"})

    return render(request, "formulario.html", {"formulario":form})


def alumnos(request):
    alunos=infoGeneral.objects.all() #este es la consulta en sql select * from
    return render(request, "alumnos.html", {"alumnos":alumnos})
# Create your views here.
