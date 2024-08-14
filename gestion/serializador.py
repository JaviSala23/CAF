# serializers.py
from rest_framework import serializers
from gestion.models import sexo

class SexoSerializer(serializers.ModelSerializer):
    class Meta:
        model = sexo
        fields = ['id', 'nombre']