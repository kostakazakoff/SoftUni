from django.db import models
from photos.models import Photo

'''
The field Comment Text is required:
• Comment Text - it should consist of a maximum of 300 characters
An additional field should be created:
• Date and Time of Publication - when a comment is created (only), the date of publication is automatically
generated
One more thing we should keep in mind is that the comment should relate to the photo (as in social apps users
comment on a specific photo/post, i.e., the comment object is always connected to the photo object).
'''


class Comment(models.Model):
    COMMENT_MAX_LENGTH = 300
    
    comment_text = models.CharField(
        max_length=COMMENT_MAX_LENGTH,
        null=True,
        blank=True,
    )
    publication_date_time = models.DateTimeField(
        auto_now_add=True,
    )
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

# class Like(models.Model):
#     to_photo = models.ForeignKey(
#         Photo,
#         on_delete=models.CASCADE,
#         null=False,
#         blank=True,
#     )
