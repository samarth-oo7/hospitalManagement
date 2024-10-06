from django import forms
from .models import Patient, Appointment

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'mobile_number', 'patient_id']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['description_of_illness', 'blood_pressure', 'body_temperature', 'diagnosis', 'medicine', 'lab_reports']
