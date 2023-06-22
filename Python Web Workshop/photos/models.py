from django.db import models
from pets.models import Pet
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from petstagram.core.utils import mbytes_to_bytes


class Photo(models.Model):
    MAX_IMG_SIZE = 5.0
    DESCRIPTION_MAX_LENGTH = 300
    DESCRIPTION_MIN_LENGTH = 10
    LOCATION_MAX_LENGTH = 30

    def validate_max_img_size(self):
        if self.file.size > mbytes_to_bytes(Photo.MAX_IMG_SIZE ):
            raise ValidationError(f'Max file size is {Photo.MAX_IMG_SIZE}MB')
        
    photo = models.ImageField(
        null=False,
        blank=False,
        upload_to='photos/',
        validators=[validate_max_img_size]
    )
    description = models.TextField(
        null=True,
        blank=True,
        max_length=DESCRIPTION_MAX_LENGTH,
        validators=[MinLengthValidator(DESCRIPTION_MIN_LENGTH,)]
    )
    location = models.CharField(
        max_length=LOCATION_MAX_LENGTH,
        null=True,
        blank=True,
    )
    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
        related_name='all_photos',
    )
    date_of_publication = models.DateField(
        auto_now=True,
    )

    @property
    def get_tagged_pets(self):
        if self.tagged_pets:
            return ', '.join(p.name for p in self.tagged_pets.all())
        return ''
