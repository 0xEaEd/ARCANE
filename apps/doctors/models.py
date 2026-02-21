from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.ForeignKey('Specialization', on_delete=models.CASCADE)

class Specialization(models.Model):
    name = models.CharField(max_length=100)

class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medication = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)