from django.db import models
from django.utils import timezone
from accounts.models import CustomUser

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
        return self.initial_date <= now <= self.end_date
    
    def is_active(self):
        return self.status
    
    is_active.boolean = True
    is_active.short_description = 'Active Status'
    
    def __str__(self):
        return self.name_event
    
class Activity(models.Model):
    title_activity = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    date_time = models.DateTimeField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='activities')
    
    def __str__(self):
        return self.title_activity
    
# Modelo para la programación de actividades seleccionadas por los usuarios
class Schedule(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_activities')
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='scheduled_activities')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'activity')
    
    def __str__(self):
        return f"{self.user.name} - {self.activity.title_activity}"
    
