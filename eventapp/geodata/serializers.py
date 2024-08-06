from rest_framework import serializers
from .models import Country, State, Municipality

class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = ['id', 'name']

class StateSerializer(serializers.ModelSerializer):
    municipalities = MunicipalitySerializer(many=True, read_only=True)

    class Meta:
        model = State
        fields = ['id', 'name', 'municipalities']

class CountrySerializer(serializers.ModelSerializer):
    states = StateSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'name', 'states']