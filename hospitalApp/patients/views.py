from django.shortcuts import render, redirect, get_object_or_404
from .forms import PatientForm, AppointmentForm
from .models import Patient, Appointment

def home(request):
    return render(request, 'patients/home.html')

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients')
    else:
        form = PatientForm()
    return render(request, 'patients/add_patient.html', {'form': form})

def add_appointment(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = patient
            appointment.save()
            return redirect('patients')
    else:
        form = AppointmentForm()
    return render(request, 'patients/add_appointment.html', {'form': form, 'patient': patient})

def search_patient(request):
    query = request.GET.get('patient_id')
    patient = None
    appointments = None
    if query:
        try:
            patient = Patient.objects.get(patient_id=query)
            appointments = Appointment.objects.filter(patient=patient)
        except Patient.DoesNotExist:
            patient = None
    return render(request, 'patients/search_patient.html', {'patient': patient, 'appointments': appointments, 'query': query})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})
