from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from rest_framework import status
from .models import CustomUser

from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class Login(APIView):
    def post(self, request, format=None):
        user = get_object_or_404(CustomUser, email = request.data['email'])
        
        if not user.check_password(request.data['password']):
            return Response({"error" : "Invalid Password"}, status=status.HTTP_400_BAD_REQUEST)
        
        token, created = Token.objects.get_or_create(user = user)
        serializer = CustomUserSerializer(instance=user)
        
        return Response({"token" : token.key, "user" : serializer.data}, status=status.HTTP_200_OK)

    
class Register(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            user = CustomUser.objects.get(email = serializer.data['email'])
            user.set_password(serializer.data['password'])
            user.save()
            
            token = Token.objects.create(user=user)
            
            return Response({'token': token.key, "user" : serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Prueba(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return Response("You are logged in with {}".format(request.user.email), status=status.HTTP_200_OK)