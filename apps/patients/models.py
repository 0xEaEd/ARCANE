from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    medical_history = models.TextField()


class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    details = models.TextField()
    date_recorded = models.DateField()


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
