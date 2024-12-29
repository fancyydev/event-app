from rest_framework import serializers
from .models import CustomUser
from geodata.models import Country, State, Municipality

class CustomUserSerializer(serializers.ModelSerializer):
    state = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    municipality = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = [
            'email', 'name', 'phone', 'municipality', 'state', 'country',
            'occupation', 'company', 'ticket', 'created', 'is_active', 'is_superuser', 'password'
        ]
        read_only_fields = ['created']

    def get_state(self, obj):
        return obj.state.name if obj.state else ""

    def get_country(self, obj):
        return obj.country.name if obj.country else ""

    def get_municipality(self, obj):
        return obj.municipality.name if obj.municipality else ""
    
    
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