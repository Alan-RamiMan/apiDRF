from django.db import models

# Create your models here.


class Project(models.Model):#Tabla base de datos
    #Colunmas de la tabla de datos↓
    title=models.CharField(max_length=200)
    description=models.TextField()
    technology=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)#Añadir por defecto automaticamente al crear 