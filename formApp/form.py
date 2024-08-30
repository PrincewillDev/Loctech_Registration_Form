from django import forms
from .models import StudentReg

class StudentForm(forms.ModelForm):

    class Meta:
        model = StudentReg
        fields = '__all__'
    
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

        labels = {
            'start_date': 'Start Date',
            'date': 'Registration Date',
        }