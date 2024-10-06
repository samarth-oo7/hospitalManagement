from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_patient, name='add_patient'),
    path('patients/', views.patient_list, name='patients'),
    path('add_appointment/<int:patient_id>/', views.add_appointment, name='add_appointment'),
    path('search/', views.search_patient, name='search_patient'),
]
