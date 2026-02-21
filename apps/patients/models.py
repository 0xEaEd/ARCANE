from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)

class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, related_name='medical_history', on_delete=models.CASCADE)
    condition = models.CharField(max_length=100)
    date_recorded = models.DateField()

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, related_name='appointments', on_delete=models.CASCADE)
    date = models.DateTimeField()
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)