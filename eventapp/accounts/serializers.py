from rest_framework import serializers
from .models import CustomUser
from geodata.models import Country, State, Municipality

class CustomUserSerializer(serializers.ModelSerializer):
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
        country = data.get('country')
        state = data.get('state')
        municipality = data.get('municipality')
        
        try:
            country = Country.objects.get(id=int(country))
        except Country.DoesNotExist:
            raise serializers.ValidationError({'country': 'Country does not exist.'})

        try:
            state = State.objects.get(id=int(state), country=country)
        except State.DoesNotExist:
            state = None

        try:
            municipality = Municipality.objects.get(id=int(municipality), state=state)
        except Municipality.DoesNotExist:
            municipality = None
            
        data['country'] = country.name
        data['state'] = state.name if state else ""
        data['municipality'] = municipality.name if municipality else ""
            
        return data
        
class CustomRegisterSerializer(serializers.ModelSerializer):
    country = serializers.CharField()
    state = serializers.CharField(allow_blank=True, required=False)
    municipality = serializers.CharField(allow_blank=True, required=False)
    
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
            state = None

        try:
            municipality = Municipality.objects.get(name=municipality_name, state=state)
        except Municipality.DoesNotExist:
            municipality = None

        data['country'] = country
        data['state'] = state
        data['municipality'] = municipality

        return data