from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from personas.serializers import PersonaSerializer
from personas.models import Persona

# Create your views here.
class PersonaViewSet(ModelViewSet):
    serializer_class = PersonaSerializer
    queryset = Persona.objects.all()