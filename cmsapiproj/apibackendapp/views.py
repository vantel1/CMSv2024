from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Patient, MedicineStock, Medicine
from .serializers import PatientSerializer, MedicineStockSerializer, MedicineSerializer

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