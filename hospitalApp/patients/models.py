from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    mobile_number = models.CharField(max_length=15)
    patient_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    description_of_illness = models.TextField()
    blood_pressure = models.CharField(max_length=10)
    body_temperature = models.CharField(max_length=10)
    diagnosis = models.TextField()
    medicine = models.TextField()
    lab_reports = models.TextField()

    def __str__(self):
        return f"Appointment for {self.patient.name} on {self.date}"
