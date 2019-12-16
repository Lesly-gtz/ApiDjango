from django.db import models

# Create your models here.
class Student(models.Model):
    nombre = models.CharField(max_length=50)
    apellidoP = models.CharField(max_length=50)
    apellidoM = models.CharField(max_length=50)

