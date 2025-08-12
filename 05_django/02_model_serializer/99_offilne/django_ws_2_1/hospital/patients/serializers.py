from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'id', 'first_name', 'last_name',
            'birth_date', 'email', 'phone_number', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']