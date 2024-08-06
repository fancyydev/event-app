from .views import Login, Register, Prueba
from django.urls import path

urlpatterns = [
    path('login', Login.as_view()),
    path('register', Register.as_view()),
    path('prueba', Prueba.as_view()),
]