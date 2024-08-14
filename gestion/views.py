from django.shortcuts import render

from gestion.models import sexo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here

@api_view(['POST'])
def guardar_sexo(request): 
    try:  
        nombre=request.data.get('nombre')
        sexo1=sexo(nombre=nombre)
        sexo1.save()
        return Response({'message': 'Se a agregado correctamente el sexo'}, status=status.HTTP_200_OK)
    except:
        # Autenticación fallida
        return Response({'message': 'Hubo un error en agregar el sexo'}, status=status.HTTP_401_UNAUTHORIZED)
                    

@api_view(['GET'])
def consultarTodoLosSexos(request):
    
    sexos=sexo.objects.all()
    serialized_data = [
        {
            'id': sexo1.id,
            'nombre': sexo1.nombre,
    
        }
        for sexo1 in sexos
    ]

    return Response(serialized_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def consultarUno(request,id):
    sexos=sexo.objects.get(pk=id)
    serialized_data = {
            'id': sexos.id,
            'nombre': sexos.nombre,
    
        }
        

    return Response(serialized_data, status=status.HTTP_200_OK)

