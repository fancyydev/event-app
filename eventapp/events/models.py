from django.db import models
from accounts.models import CustomUser
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    name_event = models.CharField(max_length=250)
    description = models.TextField()
    initial_date = models.DateField()
    end_date = models.DateField()
    program = models.FileField(upload_to='pdfs/')
    @property
    def status(self):
        now = timezone.now().date()
        print(now)
        return self.initial_date <= now <= self.end_date
    
    def is_active(self):
        return self.status
    
    is_active.boolean = True
    is_active.short_description = 'Active Status'
    
    def __str__(self):
        return self.name_event
    
    def clean(self):
        """ Validate that only one event can be active at a time """
        if self.status:
            if Event.objects.exclude(id=self.id).filter(
                initial_date__lte=timezone.now().date(), 
                end_date__gte=timezone.now().date()
            ).exists():
                raise ValidationError('There is already an active event. Please select different dates.')
        super().clean()
    
    def save(self, *args, **kwargs):
        self.clean()
        super(Event, self).save(*args, **kwargs)
    
class Sponsor(models.Model):
    name = models.CharField(max_length=250, verbose_name="Sponsor Name")
    link = models.URLField(max_length=500, verbose_name="Sponsor Link")
    logo = models.ImageField(upload_to='sponsors/logos/', verbose_name="Sponsor Logo")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_sponsors')

    def __str__(self):
        return self.name
    
class Room(models.Model):
    name_room = models.CharField(max_length=250)
    # Relacionar habitaciones con event
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='rooms', null=True, blank=True)  # Relacionar habitaciones con eventos

    def __str__(self):
        return self.name_room
    
class Activity(models.Model):
    title_activity = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    date_time = models.DateTimeField()
    author = models.CharField(max_length=250, default="-")
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_activities')
    # Como puedo hacer para mostrar solo los cuartos que pertenecen al event seleccionado en el admin
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='rooms_activities')
    
    #Hacer un clean que verifique si el event relacionado con room es el mismo que el de event si no marcar error
    def __str__(self):
        return self.title_activity
    
# Modelo para la programación de actividades seleccionadas por los usuarios
class Schedule(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='scheduled_user')
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='scheduled_activities')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'activity')
    
    def __str__(self):
        return f"{self.user.name} - {self.activity.title_activity}"
    
