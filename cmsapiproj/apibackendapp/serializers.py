from rest_framework import serializers
from .models import Patient, MedicineStock, Medicine
from .models import MedicinePrescription, LabTestPrescription
from .models import Consultation

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


class MedicinePrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicinePrescription
        fields = '__all__'


class LabTestPrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestPrescription
        fields = ("AppointmentId", "LabTestId", "LabTestValue", "Remarks")


class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'