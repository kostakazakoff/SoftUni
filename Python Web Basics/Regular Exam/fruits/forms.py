from django import forms
from .models import Fruit


class CreateFruit(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""

    class Meta:
        model = Fruit
        fields = ['name', 'image_url', 'description', 'nutrition']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name', 'maxlength': 30}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'}),
        }


class EditFruit(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['name', 'image_url', 'description', 'nutrition']
        widgets = {
            'name': forms.TextInput(attrs={'maxlength': 30}),
        }


class DeleteFruit(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['name', 'image_url', 'description']
