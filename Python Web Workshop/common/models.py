from django.db import models
from photos.models import Photo


class PhotoComment(models.Model):
    COMMENT_MAX_LENGTH = 300

    comment_text = models.TextField(
        max_length=COMMENT_MAX_LENGTH,
        null=False,
        blank=False,
    )
    publication_date_time = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=True,
        null=False,
    )
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

class PhotoLike(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
        related_name='all_photo_likes',
    )
    # TODO: When the Users model is created
    # to_user = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     related_name='user_photo_like',
    # )
