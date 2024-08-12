from rest_framework import serializers
from .models import CustomUser
from geodata.models import Country, State, Municipality

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'email', 'name', 'phone', 'municipality', 'state', 'country',
            'occupation', 'company', 'ticket', 'created', 'is_active', 'is_superuser', 'password'
        ]
        read_only_fields = ['created']
        
        
class CustomRegisterSerializer(serializers.ModelSerializer):
    country = serializers.CharField()
    state = serializers.CharField()
    municipality = serializers.CharField()
    
    class Meta:
        model = CustomUser
        fields = [
            'email', 'name', 'phone', 'municipality', 'state', 'country',
            'occupation', 'company', 'ticket', 'created', 'is_active', 'is_superuser', 'password'
        ]
        read_only_fields = ['created']
    
    def validate(self, data):
        # Validar y asignar país
        country_name = data.get('country')
        state_name = data.get('state')
        municipality_name = data.get('municipality')

        try:
            country = Country.objects.get(name=country_name)
        except Country.DoesNotExist:
            raise serializers.ValidationError({'country': 'Country does not exist.'})

        try:
            state = State.objects.get(name=state_name, country=country)
        except State.DoesNotExist:
            raise serializers.ValidationError({'state': 'State does not exist for the given country.'})

        try:
            municipality = Municipality.objects.get(name=municipality_name, state=state)
        except Municipality.DoesNotExist:
            raise serializers.ValidationError({'municipality': 'Municipality does not exist for the given state.'})

        data['country'] = country
        data['state'] = state
        data['municipality'] = municipality

        return data