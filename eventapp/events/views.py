from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Event, Activity, Schedule
from .serializers import ActivityListSerializer, ActivityUserSelectionSerializer
from accounts.models import CustomUser


# Create your views here.

class ActivityListView(APIView):
    #El slug tiene que ser siempre el tercer parametro de la funcion get
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        if Activity.objects.all().exists():
            results = Activity.objects.all()
            print(results)
            serializer = ActivityListSerializer(results, many=True)
            print(serializer.data)
            return Response({'activities': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No categories found'}, status=status.HTTP_404_NOT_FOUND)

class ActivityListByUser(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request, id_user, format=None):
        # Obtener el usuario de la base de datos (asegúrate de manejar la excepción si el usuario no existe)
        try:
            user = CustomUser.objects.get(pk=id_user)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Obtener todas las actividades
        activities = Activity.objects.all()

        # Serializar las actividades y pasar el usuario en el contexto
        serializer = ActivityUserSelectionSerializer(activities, many=True, context={'user': user})
        
        return Response({'activities': serializer.data}, status=status.HTTP_200_OK)

        
        