from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Patient, MedicineStock, Medicine
from .serializers import PatientSerializer, MedicineStockSerializer, MedicineSerializer
from .models import MedicinePrescription, LabTestPrescription
from .serializers import MedicinePrescriptionSerializer, LabTestPrescriptionSerializer
from .models import Consultation
from .serializers import ConsultationSerializer

# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
    permission_classes = [ AllowAny ]

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    def create(self, req):
        serializer = PatientSerializer(data = req.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "message": "Patient registered successfully"
        }, status=status.HTTP_201_CREATED)

class MedicineStockViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = MedicineStock.objects.all()
    serializer_class = MedicineStockSerializer


class MedicineViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer


class MedicinePrescriptionViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = MedicinePrescription.objects.all()
    serializer_class = MedicinePrescriptionSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "Medicine prescription created successfully."},
            status=status.HTTP_201_CREATED,
        )

    def patch(self, request):
        serializer = self.get_serializer(data=request.data)
        serailizer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "Medicine Prescription updated successfully."},
            status=status.HTTP_200_OK,
        )


class LabTestPrescriptionViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = LabTestPrescription.objects.all()
    serializer_class = LabTestPrescriptionSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "Lab Test prescription createed successfully."},
            status=status.HTTP_201_CREATED,
        )

    def patch(self, request):
        serializer = self.get_serializer(data=request.data)
        serailizer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "Lab Test Prescription updated successfully."},
            status=status.HTTP_200_OK,
        )
    

class ConsultationViewSet(viewsets.ModelViewSet):
    permission_classes = [ AllowAny ]

    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    def create(self, req):
        serializer = ConsultationSerializer(data = req.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "message": "Consultation note added successfully"
        }, status=status.HTTP_201_CREATED)

