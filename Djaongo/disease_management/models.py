from django.db import models

class PatientRecord(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Urgent', 'Urgent'),
    ]

    patient_cnic = models.CharField(max_length=15, unique=True) # 1
    patient_name = models.CharField(max_length=100) # 2
    cellphone = models.CharField(max_length=15) # 3
    disease = models.CharField(max_length=200) # 4
    day = models.DateField() # 5
    time = models.TimeField() # 6
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium') # 7
    status = models.CharField(max_length=20, default="Pending") # 8 (Status attribute)

    def __str__(self):
        return f"{self.patient_name} - {self.disease}"
