from django.db import models
from django.utils.text import slugify

'''
Name - it should consist of a maximum of 30 characters.
• Personal Pet Photo - the user can link a picture using a URL
The field date of birth is optional:
• Date of Birth - pet's day, month, and year of birth
Slug - a slug automatically generated using the pet's name and the pet's id, separated by a "-" (dash).
'''

class Pet(models.Model):
    name = models.CharField(
        max_length=30,
        )
    personal_photo = models.URLField()
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    slug = models.SlugField(
        unique=True,
    )

    # Auto generate slug
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')

        return super().save(*args, **kwargs)
