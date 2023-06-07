from django.db import models
from django.core.exceptions import ValidationError
from petstagram.core.utils import mbytes_to_bytes
from django.core.validators import MinLengthValidator
from pets.models import Pet

'''
The field Photo is required:
• Photo - the user can upload a picture from storage, the maximum size of the photo can be 5MB
The fields description and tagged pets are optional:
• Description - a user can write any description of the photo; it should consist of a maximum of 300 characters
and a minimum of 10 characters
• Location - it should consist of a maximum of 30 characters
• Tagged Pets - the user can tag none, one, or many of all pets. There is no limit on the number of tagged pets
There should be created one more field that will be automatically generated:
• Date of publication - when a picture is added or edited, the date of publication is automatically generated
'''

class Photo(models.Model):
    MAX_IMG_SIZE = 1.0
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
    description = models.CharField(
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
