from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.exceptions import NotFound

from .models import Event, Activity, Schedule, Sponsor
from .serializers import ActivityListSerializer, ActivityUserSelectionSerializer, ScheduleSerializer, SponsorSerializer, EventSerializer, EventImageSerializer
from accounts.models import CustomUser

from django.utils import timezone

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from django.http import FileResponse, Http404
from django.db.models import Case, When, IntegerField
# Create your views here.

# class ActivityListView(APIView):
#     #El slug tiene que ser siempre el tercer parametro de la funcion get
#     permission_classes = (permissions.AllowAny,)
#     def get(self, request, format=None):
#         if Activity.objects.all().exists():
#             results = Activity.objects.all()
#             serializer = ActivityListSerializer(results, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'No categories found'}, status=status.HTTP_404_NOT_FOUND)

# class ActivityListByUser(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
    
#     def get(self, request, format=None):
#         # Obtener el usuario de la base de datos (asegúrate de manejar la excepción si el usuario no existe)
#         try:
#             #user = CustomUser.objects.get(pk=id_user)
#             user = request.user
#         except CustomUser.DoesNotExist:
#             return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

#         # Obtener todas las actividades
#         activities = Activity.objects.all()

#         # Serializar las actividades y pasar el usuario en el contexto
#         serializer = ActivityUserSelectionSerializer(activities, many=True, context={'user': user})
        
#         return Response(serializer.data, status=status.HTTP_200_OK)

class ActiveEvent(APIView):
    def get(self, request, format=None):
        now = timezone.localtime(timezone.now()).date()  # Convertir a la hora local
        event = Event.objects.filter(initial_date__lte=now, end_date__gte=now).first()
        if event is None:
            return Response({
                "id": -1,
                "name_event": "",
                "description": "",
                "initial_date": "",
                "end_date": "",
                "logo_url": "",
                "is_active": None
                }, status=status.HTTP_200_OK)
            
        serializer = EventSerializer(event, many=False, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class ActiveSponsorsEvent(APIView):
    def get(self, request, format=None):
        now = timezone.localtime(timezone.now()).date()
        event = Event.objects.filter(initial_date__lte=now, end_date__gte=now).first()
        
        if event is None:
            raise NotFound("Event not found.")
        
        sponsors = Sponsor.objects.filter(event=event).annotate(
            tier_order=Case(
                When(tier='diamante', then=1),
                When(tier='platino', then=2),
                When(tier='oro', then=3),  # Si decides agregar 'gold'
                When(tier='plata', then=4),
                When(tier='patrocinador', then=5),
                default=6,
                output_field=IntegerField(),
            )
        ).order_by('tier_order')
        
        if not sponsors.exists():
            raise NotFound('No sponsors found for this event.')
        
        serializer = SponsorSerializer(sponsors, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class ActiveProgramEvent(APIView):
    def get(self, request, format=None):
        now = timezone.localtime(timezone.now()).date()
        event = Event.objects.filter(initial_date__lte=now, end_date__gte=now).first()
        if event == None:
            raise NotFound("Event not found.")
        if event.program:
            return FileResponse(event.program.open(), as_attachment=True, filename=event.program.name)
        else:
            return Response({"detail": "No program found for this event."}, status=status.HTTP_404_NOT_FOUND)
        
class ActiveEventImages(APIView):
    def get(self, request, format=None):
        now = timezone.localtime(timezone.now()).date()
        event = Event.objects.filter(initial_date__lte=now, end_date__gte=now).first()
        if event == None:
            raise NotFound("Event not found.")
        images = event.event_images.filter(event = event).order_by('id')
        if not images.exists():
            raise NotFound('No images found for this event.')
            
        serializer = EventImageSerializer(images, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class ActiveActivityListByUser(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        # Obtener el usuario de la base de datos (asegúrate de manejar la excepción si el usuario no existe)
        try:
            user = request.user
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        now = timezone.localtime(timezone.now()).date()
        event = Event.objects.filter(initial_date__lte=now, end_date__gte=now).first()
        if event is None:
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Ordenar las actividades por id
        activities = Activity.objects.filter(event=event).order_by('id')
        serializer = ActivityUserSelectionSerializer(activities, many=True, context={'user': user})
        
        return Response( serializer.data, status=status.HTTP_200_OK)


class AssignUserActivity(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    
    def post(self, request, id_activity, format=None):
        try:
            user = request.user
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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, id_activity, format=None):
        try:
            user = request.user
            activity = Activity.objects.get(id=id_activity)
            schedule = Schedule.objects.get(user=user, activity=activity)
            schedule.delete()
            return Response({"detail": "Activity successfully unscheduled."}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Activity.DoesNotExist:
            return Response({'error': 'Activity not found'}, status=status.HTTP_404_NOT_FOUND)
        except Schedule.DoesNotExist:
            return Response({"error": "Schedule entry not found."}, status=status.HTTP_404_NOT_FOUND)