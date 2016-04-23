from rest_framework.serializers import ModelSerializer
from personas.models import Persona

class PersonaSerializer(ModelSerializer):
    class Meta:
        model = Persona
        ordering = ('-nombre')
        fields = ('id', 'nombre', 'descripcion', 'foto', 'habilidad_uno', 'habilidad_dos',
                  'habilidad_tres')
