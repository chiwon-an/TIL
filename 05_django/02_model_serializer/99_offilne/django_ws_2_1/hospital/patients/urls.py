from django.urls import path
from .views import PatientListCreateView, PatientRetrieveUpdateDeleteView

urlpatterns = [
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientRetrieveUpdateDeleteView.as_view(), name='patient-rud'),
]