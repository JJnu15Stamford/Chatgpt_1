from  import forms
from django.core.exceptions import ValidationError
import re

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        required=True,
        label='Full Name',
        widget=forms.TextInput(attrs={'placeholder': 'Your Name'}),
        error_messages={
            'required': 'Please enter your name.',
            'max_length': 'Name must be under 50 characters.'
        }
    )

    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}
        )
    )