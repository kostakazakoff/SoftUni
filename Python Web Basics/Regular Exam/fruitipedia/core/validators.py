from django.core.exceptions import ValidationError


def validate_name_start_with_letter(value: str):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")
    

def validate_name_all_letters(value: str):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")