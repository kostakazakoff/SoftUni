from django.shortcuts import render
from photos.models import Photo

def apply_user_liked_photo(photo):
    return photo.all_photo_likes.count()

def home_view(request):
    photos = [apply_user_liked_photo(p) for p in Photo.objects.all()]
    context = {
        'photos': photos,
    }
    return render(request, 'common/home-page.html', context)
