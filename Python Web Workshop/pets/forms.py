from django import forms
from .models import Pet


class PetCreateForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ('slug',)