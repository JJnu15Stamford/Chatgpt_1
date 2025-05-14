from import forms
from django.core import ValidationError
import readline

class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        required=True,
        label='Username',
        widget=forms.TextInput(attrs={'placeholder': 'Enter username'}),
        error_messages={
            'required': 'Username is required.',
            'max_length': 'Username cannot exceed 30 characters.'
        }
    )