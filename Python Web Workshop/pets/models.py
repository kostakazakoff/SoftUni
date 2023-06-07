from django.db import models
from django.utils.text import slugify


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
        editable=False,
        blank=True,
    )

    def __str__(self):
        return self.slug

    @property
    def photos_count(self):
        return self.photos.count()

    # Auto generate slug
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')

        return super().save(*args, **kwargs)
