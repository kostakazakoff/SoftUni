from django.shortcuts import render
from .models import Pet

def add_pet(request):
    return render(request, 'pets/pet-add-page.html')

def delete_pet(request, username, pet_slug):
    return render(request, 'pets/pet-delete-page.html')

def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    pet_all_photos = pet.photos.all()
    context = {
        'pet': pet,
        'all_photos': pet_all_photos,
        'username': username,
    }
    return render(request, 'pets/pet-details-page.html', context)

def edit_pet(request, username, pet_slug):
    return render(request, 'pets/pet-edit-page.html')
