from django.contrib import admin
from .models import Event, Activity, Schedule

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name_event', 'initial_date', 'end_date', 'program', 'is_active']
    list_filter = ['initial_date', 'end_date']
    search_fields = ['name_event', 'description']
    
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['title_activity', 'slug', 'date_time', 'event']
    list_filter = ['date_time', 'event']
    search_fields = ['title_activiy', 'description', 'event']
    prepopulated_fields = {'slug':('title_activity',)}
    
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity', 'created_at']
    list_filter = ['user', 'activity', 'created_at']
    search_fields = ['user', 'activity']
