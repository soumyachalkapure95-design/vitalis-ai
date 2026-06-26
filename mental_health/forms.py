from django import forms
from .models import MoodLog

class MoodLogForm(forms.ModelForm):
    class Meta:
        model = MoodLog
        fields = ['mood', 'notes']
        widgets = {
            'mood': forms.Select(attrs={'class': 'form-select form-control-custom'}),
            'notes': forms.Textarea(attrs={'class': 'form-control form-control-custom', 'rows': 3, 'placeholder': 'Write down how you feel or what made you feel this way...'}),
        }
