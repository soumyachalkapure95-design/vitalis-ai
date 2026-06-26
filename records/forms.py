from django import forms
from .models import HealthRecord

class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ['age', 'blood_group', 'allergies', 'medications']
        widgets = {
            'allergies': forms.Textarea(attrs={'rows': 3, 'placeholder': 'e.g. Peanuts, Penicillin (leave blank if none)'}),
            'medications': forms.Textarea(attrs={'rows': 3, 'placeholder': 'e.g. Aspirin 100mg daily, Metformin 500mg twice daily'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control form-control-custom'})
