from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Event, Activity, Schedule
from .serializers import ActivityListSerializer, ActivityUserSelectionSerializer, ScheduleSerializer
from accounts.models import CustomUser

from django.utils import timezone

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

class ActiveActivityListByUser(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request, id_user, format=None):
        # Obtener el usuario de la base de datos (asegúrate de manejar la excepción si el usuario no existe)
        try:
            user = CustomUser.objects.get(pk=id_user)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        now  = timezone.now().date()
         
        event = Event.objects.filter(initial_date__lte=now, end_date__gte=now).first()
        if (event == None):
            return Response({'error': 'Event not found'})
        
        activities = Activity.objects.filter(event = event)
        serializer = ActivityUserSelectionSerializer(activities, many=True, context={'user': user})
        
        return Response({'activities': serializer.data}, status=status.HTTP_200_OK)


class AssignUserActivity(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, id_user, id_activity, format=None):
        try:
            user = CustomUser.objects.get(pk=id_user)
            activity = Activity.objects.get(id=id_activity)
            schedule, created = Schedule.objects.get_or_create(user=user, activity=activity)
            if created:
                return Response(ScheduleSerializer(schedule).data, status=status.HTTP_201_CREATED)
            else:
                return Response({"detail": "Activity is already scheduled."}, status=status.HTTP_200_OK)
       
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Activity.DoesNotExist:
            return Response({'error': 'Activity not found'}, status=status.HTTP_404_NOT_FOUND)

class RemoveUserActivity(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def delete(self, request, id_user, id_activity, format=None):
        try:
            user = CustomUser.objects.get(pk=id_user)
            activity = Activity.objects.get(id=id_activity)
            schedule = Schedule.objects.get(user=user, activity=activity)
            schedule.delete()
            return Response({"detail": "Activity successfully unscheduled."}, status=status.HTTP_204_NO_CONTENT)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Activity.DoesNotExist:
            return Response({'error': 'Activity not found'}, status=status.HTTP_404_NOT_FOUND)
        except Schedule.DoesNotExist:
            return Response({"error": "Schedule entry not found."}, status=status.HTTP_404_NOT_FOUND)