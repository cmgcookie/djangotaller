from django.db import models

# Create your models here.
class infoGeneral(models.Model):
    nombre = models.CharField(max_length = 50, default = "Cookie")
    apellido = models.CharField(blank=True, max_length = 50, default="")
    telefono = models.CharField(max_length=50)
    fecha_nac = models.DateField(blank=True, null=True)
    semestre = models.IntegerField()
    carrera = models.CharField(max_length=50)
    SEXO_OPTIONS = (
        ('F','Femenino'),
        ('M','Masculino'),
    )
    sexo = models.CharField(blank=True, max_length=2, choices=SEXO_OPTIONS)
    direccion = models.CharField(blank=True, max_length=100)
    estatura = models.CharField(blank=True, max_length=50, default="")
    email = models.EmailField(default="")
    edad = models.IntegerField(default=18)