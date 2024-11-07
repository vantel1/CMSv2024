from rest_framework import serializers
from .models import Patient, MedicineStock, Medicine

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class MedicineStockSerializer(serializers.ModelSerializer):
    class Meta :
        model = MedicineStock
        fields = '__all__'

class MedicineSerializer(serializers.ModelSerializer):
    class Meta :
        model = Medicine
        fields = '__all__'