from rest_framework import serializers
from .models import Event, Activity, Schedule, Sponsor

class EventSerializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()
    class Meta:
        model = Event
        fields = [
            'id',
            'name_event',
            'description',
            'initial_date',
            'end_date',
            'logo_url',
            'is_active',
        ]
    def get_logo_url(self, obj):
        request = self.context.get('request')
        if obj.logo and hasattr(obj.logo, 'url'):
            return request.build_absolute_uri(obj.logo.url)
        return None

class ActivityListSerializer(serializers.ModelSerializer):
    date_time = serializers.SerializerMethodField()
    room = serializers.SerializerMethodField()
    class Meta:
        model = Activity
        fields = [
            'id',
            'title_activity',
            'slug',
            'description',
            'date_time',
            'author',
            'event',
            'room',
        ]
    def get_date_time(self, obj):
        return obj.get_activity_datetime_range()
    def get_room(self,obj):
        return obj.room.name_room

class ActivityUserSelectionSerializer(serializers.ModelSerializer):
    is_selected = serializers.SerializerMethodField()
    date_time = serializers.SerializerMethodField()
    room = serializers.SerializerMethodField()
    
    class Meta:
        model = Activity
        fields = ['id', 'title_activity', 'slug', 'description', 'date_time', 'author', 'event', 'room', 'is_selected']

    def get_date_time(self, obj):
        return obj.get_activity_datetime_range()
    
    def get_is_selected(self, obj):
        user = self.context['user']
        #Agregar al contexto el evento
        return obj.scheduled_activities.filter(user=user).exists()
    
    def get_room(self,obj):
        return obj.room.name_room
    
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'user', 'activity', 'created_at']
        
class SponsorSerializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()

    class Meta:
        model = Sponsor
        fields = ['name', 'link', 'logo_url', 'event']

    def get_logo_url(self, obj):
        request = self.context.get('request')
        if obj.logo and hasattr(obj.logo, 'url'):
            return request.build_absolute_uri(obj.logo.url)
        return None