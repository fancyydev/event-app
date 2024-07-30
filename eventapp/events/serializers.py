from rest_framework import serializers
from .models import Event, Activity, Schedule

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'name_event',
            'description',
            'initial_date',
            'end_date',
            'is_active',
        ]

class ActivityListSerializer(serializers.ModelSerializer):
    event = EventSerializer()
    class Meta:
        model = Activity
        fields = [
            'id',
            'title_activity',
            'slug',
            'description',
            'date_time',
            'event',
        ]
        
class ActivityUserSelectionSerializer(serializers.ModelSerializer):
    is_selected = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['id', 'title_activity', 'slug', 'description', 'date_time', 'event', 'is_selected']

    def get_is_selected(self, obj):
        user = self.context['user']
        return obj.scheduled_activities.filter(user=user).exists()