from django.db import models
from django.core.validators import MinLengthValidator
from fruitipedia.core.validators import validate_name_start_with_letter


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        null=False,
        blank=False,
        validators=[MinLengthValidator(2), validate_name_start_with_letter],
    )
    last_name = models.CharField(
        max_length=35,
        null=False,
        blank=False,
        validators=[MinLengthValidator(1), validate_name_start_with_letter],
    )
    email = models.EmailField(
        null=False,
        blank=False,
        max_length=40,
    )
    password = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=[MinLengthValidator(8)],
    )
    image_url = models.URLField(
        null=True,
        blank=True,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
