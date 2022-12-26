from rest_framework import serializers
from .models import Project

#Convertir las peticiones a JSON?

class ProjectSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Project
        fields=('id','title','description','technology','created_at')
        read_only_fields=('created_at',)#Campos de solo lectura