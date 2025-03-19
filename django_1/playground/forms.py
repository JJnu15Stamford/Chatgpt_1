from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Once the form is valid, we can process the data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return render(request, 'contact_result.html', {'name': name, 'email': email})
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})
