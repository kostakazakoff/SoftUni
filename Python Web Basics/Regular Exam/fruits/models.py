from django.db import models
from django.core.validators import MinLengthValidator
from fruitipedia.core.validators import validate_name_all_letters


class Fruit(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=[MinLengthValidator(2), validate_name_all_letters],
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    nutrition = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
