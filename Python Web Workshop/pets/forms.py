from django import forms
from .models import Pet


class PetCreateForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_photo']
        labels = {
            'name': 'Pet Name',
            'personal_photo': 'Link to Image',
            'date_of_birth': 'Date of Birth',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet Name'}),
            'personal_photo': forms.TextInput(attrs={'placeholder': 'Link to Image'}),
            'date_of_birth': forms.DateInput(attrs={'placeholder': 'dd/mm/yyyy', 'type': 'date'}),
        }