from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'email', 'name', 'phone', 'municipality', 'state', 'country',
            'occupation', 'company', 'ticket', 'created', 'is_active', 'is_superuser', 'password'
        ]
        read_only_fields = ['created']