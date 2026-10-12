from django.shortcuts import render, redirect
from .forms import PatientForm
from .models import PatientRecord  # <--- Ye line lazmi add karein

def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list') # List par jane ke liye
    else:
        form = PatientForm()
    return render(request, 'add_patient.html', {'form': form})

# Ye function bhi add karein taake 'list' wala error na aaye
def patient_list(request):
    patients = PatientRecord.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})