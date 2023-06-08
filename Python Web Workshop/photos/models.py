from django.db import models
from django.core.exceptions import ValidationError
from petstagram.core.utils import mbytes_to_bytes
from django.core.validators import MinLengthValidator
from pets.models import Pet


class Photo(models.Model):
    MAX_IMG_SIZE = 5.0
    DESCRIPTION_MAX_LENGTH = 300
    DESCRIPTION_MIN_LENGTH = 10
    LOCATION_MAX_LENGTH = 30

    def validate_max_img_size(self):
        if self.file.size > mbytes_to_bytes(Photo.MAX_IMG_SIZE):
            raise ValidationError(f'Max file size is {Photo.MAX_IMG_SIZE}MB')
        
    photo = models.ImageField(
        upload_to='images',
        validators=[validate_max_img_size],
        null=False,
        blank=False,
    )
    description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
        validators=[MinLengthValidator(DESCRIPTION_MIN_LENGTH)],
        blank=True,
        null=True,
    )
    location = models.CharField(
        max_length=LOCATION_MAX_LENGTH,
        blank=True,
        null=True,
    )
    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
        related_name='photos',
    )
    date_of_publication = models.DateField(
        auto_now=True,
    )

    def __str__(self):
        return str(self.photo)