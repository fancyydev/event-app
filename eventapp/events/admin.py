from django.contrib import admin
from .models import Event, Activity, Schedule, Room, Sponsor

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['id','name_event', 'initial_date', 'end_date', 'program', 'is_active']
    list_filter = ['initial_date', 'end_date']
    search_fields = ['name_event', 'description']

class RoomAdmin(admin.ModelAdmin):
    list_display = ('id','name_room',)

class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'title_activity', 'slug', 'start_datetime', 'end_datetime', 'event', 'room']
    list_filter = ['start_datetime', 'event']
    search_fields = ['title_activity', 'description', 'event']
    prepopulated_fields = {'slug': ('title_activity',)}

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'activity', 'created_at']
    list_filter = ['user', 'activity', 'created_at']
    search_fields = ['user', 'activity']


class SponsorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'link']
    list_filter = ['name', 'link']
    search_fields = ['name', 'link']
    
    
# Register the models in the desired order
admin.site.register(Event, EventAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Sponsor, SponsorAdmin)


