from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'role',
            'phone',
            'date_of_birth',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control form-control-custom'})
            if field_name == 'date_of_birth':
                field.widget = forms.DateInput(attrs={
                    'class': 'form-control form-control-custom',
                    'type': 'date'
                })