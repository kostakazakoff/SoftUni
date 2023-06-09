from django.shortcuts import render
from .models import Photo

def add_photo(request):
    return render(request, 'photos/photo-add-page.html')

def details_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.all_photo_likes.count()
    comments = photo.photo_comments.all()
    context = {'photo': photo, 'likes': likes, 'comments': comments}

    return render(request, 'photos/photo-details-page.html', context=context)

def edit_photo(request, pk):
    return render(request, 'photos/photo-edit-page.html')