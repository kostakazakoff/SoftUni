from django import forms
from .models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'maxlength': 25}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'maxlength': 35}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'maxlength': 40}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password', 'maxlength': 20}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'image_url', 'age']