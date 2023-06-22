from django.db import models
from photos.models import Photo


class Comment(models.Model):
    COMMENT_MAX_LENGTH = 300

    comment_text = models.TextField(
        max_length=COMMENT_MAX_LENGTH,
        null=False,
        blank=False,
    )
    date_of_publication = models.DateTimeField(
        auto_now_add=True,
    )
    to_photo = models.ForeignKey(
        Photo,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='photo_comments',
    )


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='photo_likes',
    )
    # TODO: When User is created
    # user = models.ForeignKey(User)
