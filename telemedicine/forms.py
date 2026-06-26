from django import forms
from .models import Appointment
from accounts.models import CustomUser

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time_slot', 'symptoms']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'symptoms': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe symptoms or reasons for appointment...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limit doctor choices to only users with 'doctor' role
        self.fields['doctor'].queryset = CustomUser.objects.filter(role='doctor')
        
        # Apply CSS classes
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control form-control-custom'})
