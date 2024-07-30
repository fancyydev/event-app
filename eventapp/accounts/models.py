from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

#Un manager me permite definir funciones que puedan realizar consultas
class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, phone, municipality, state, country, occupation, company, password = None):
        if not email:
            raise ValueError('EL USUARIO DEBE TENER UN CORREO ELECTRONICO')
        
        usuario = self.model(
            email = self.normalize_email(email), 
            name = name, 
            phone = phone,
            municipality = municipality,
            state = state,
            country = country,
            occupation = occupation,
            company = company
            )
        
        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self, email, name, phone, municipality, state, country, occupation, company, password = None):
        usuario = self.create_user(
            email = email, 
            name = name, 
            phone = phone,
            municipality = municipality,
            state = state,
            country = country,
            occupation = occupation,
            company = company,
            password = password
        )
        
        usuario.is_superuser = True
        usuario.save()
        
        return usuario
        

# Create your models here.
class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    municipality = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    ticket = models.IntegerField(null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone', 'municipality', 'state', 'country', 'occupation', 'company']
    
    def __str__(self):
        return f'Usuario {self.name}'
    
    def has_perm(self,perm,obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True 
    
    @property
    def is_staff(self):
        return self.is_superuser