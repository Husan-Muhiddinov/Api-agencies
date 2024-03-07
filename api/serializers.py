from rest_framework import serializers
from .models import AgencyModel, FacilityModel


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityModel
        fields = '__all__'


class AgencySerializer(serializers.ModelSerializer):
    facilities = FacilitySerializer(many=True, read_only=True)

    class Meta:
        model = AgencyModel
        fields = '__all__'
