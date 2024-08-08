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

from django.core.mail import send_mail

#Imports necesarios para recuperar contraseña mediante api
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.conf import settings
from django.urls import reverse

class Login(APIView):
    def post(self, request, format=None):
        user = get_object_or_404(CustomUser, email = request.data['email'])
        
        if not user.check_password(request.data['password']):
            return Response({"error" : "Invalid Password"}, status=status.HTTP_400_BAD_REQUEST)
        
        token, created = Token.objects.get_or_create(user = user)
        serializer = CustomUserSerializer(instance=user)
        
        return Response({"token" : token.key, "user" : serializer.data}, status=status.HTTP_200_OK)

    
class Register(APIView):
    def post(self, request, format = None):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            user = CustomUser.objects.get(email = serializer.data['email'])
            user.set_password(serializer.data['password'])
            user.save()
            
            token = Token.objects.create(user=user)
            
            return Response({'token': token.key, "user" : serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PasswordRecovery(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')

        # Verifica si el correo existe en la base de datos
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({"detail": "User with this email does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        # Genera el token de recuperación de contraseña
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        # Construye la URL de recuperación
        password_reset_url = request.build_absolute_uri(
            reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
        )

        # Renderiza el mensaje del correo
        context = {
            'user': user,
            'password_reset_url': password_reset_url,
        }
        email_subject = 'Password Reset Request'
        email_body = render_to_string('password_reset_email.html', context)

        # Envía el correo electrónico
        send_mail(
            email_subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            html_message=email_body 
        )

        return Response({"detail": "Password reset email has been sent."}, status=status.HTTP_200_OK)
