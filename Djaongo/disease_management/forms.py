from django import forms
from .models import PatientRecord

class PatientForm(forms.ModelForm):
    class Meta:
        model = PatientRecord
        fields = ['patient_cnic', 'patient_name', 'cellphone', 'disease', 'day', 'time', 'priority', 'status']
        widgets = {
            'day': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }