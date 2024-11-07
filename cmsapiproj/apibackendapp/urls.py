from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'patients', views.PatientViewSet)
router.register(r'inventory/medicine', views.MedicineStockViewSet)
router.register(r'medicines', views.MedicineViewSet)
router.register(r"prescriptions/medicine", views.MedicinePrescriptionViewSet)
router.register(r"prescriptions/labtest", views.LabTestPrescriptionViewSet)

urlpatterns = router.urls
