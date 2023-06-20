from django.shortcuts import render

def pet_add(request):
    return render(request, 'pet-add-page.html')

def pet_details(request):
    return render(request, 'pet-details-page.html')

def pet_edit(request):
    return render(request, 'pet-edit-page.html')

def pet_delete(request):
    return render(request, 'pet-delete-page.html')
