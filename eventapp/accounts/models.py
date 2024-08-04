from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from geodata.models import Country, State, Municipality

# Un manager para definir funciones de creación de usuarios y superusuarios
class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, phone, occupation, company, municipality=None, state=None, country=None, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone,
            municipality=municipality,
            state=state,
            country=country,
            occupation=occupation,
            company=company
        )
        
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, name, phone, occupation, company, municipality=None, state=None, country=None, password=None):
        user = self.create_user(
            email=email,
            name=name,
            phone=phone,
            municipality=municipality,
            state=state,
            country=country,
            occupation=occupation,
            company=company,
            password=password
        )
        
        user.is_superuser = True
        user.save()
        
        return user

# Modelo de usuario personalizado
class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    
    municipality = models.ForeignKey(Municipality, on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    
    occupation = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    ticket = models.IntegerField(null=True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone','occupation', 'company']
    
    def __str__(self):
        return self.name
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_superuser