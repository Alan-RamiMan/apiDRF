from .models import Project 
from rest_framework import viewsets,permissions
from .serializers import ProjectSerializer

#Gestiona cual es la informacion que se va a mostrar y quienes pueden verla 

class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    permission_classes=[permissions.AllowAny]#cualquier cliente o aplicacion cliente puede pedir datos
    serializer_class=ProjectSerializer