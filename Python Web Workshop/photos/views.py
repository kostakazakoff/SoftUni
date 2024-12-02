from django.shortcuts import render
from .models import Photo

def photo_add(request):
    return render(request, 'photos/photo-add-page.html')

def photo_details(request, pk):
    photo = Photo.objects.filter(pk=pk).first()
    tagged_pets = photo.tagged_pets.all()
    context = {'photo': photo, 'tagged_pets': tagged_pets}
    return render(request, 'photos/photo-details-page.html', context)

def photo_edit(request, pk):
    return render(request, 'photos/photo-edit-page.html')
