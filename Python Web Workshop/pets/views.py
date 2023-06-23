from django.shortcuts import render, redirect
from petstagram.core.utils import get_pet_by_name_and_slug
from .forms import PetCreateForm


def pet_add(request):
    form = PetCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile details', pk=1) # TODO: user hardcode

    context = {'form': form}
    return render(request, 'pets/pet-add-page.html', context)


def pet_details(request, username, pet_slug):
    pet = get_pet_by_name_and_slug(pet_slug, username)
    total_photos_count = pet.all_photos.count()
    context = {'pet': pet, 'total_photos_count': total_photos_count}
    return render(request, 'pets/pet-details-page.html', context)

def pet_edit(request, username, pet_slug):
    return render(request, 'pets/pet-edit-page.html')

def pet_delete(request, username, pet_slug):
    return render(request, 'pets/pet-delete-page.html')
