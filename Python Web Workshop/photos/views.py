from django.shortcuts import render

def photo_add(request):
    return render(request, 'photo-add-page.html')

def photo_details(request):
    return render(request, 'photo-details-page.html')

def photo_edit(request):
    return render(request, 'photo-edit-page.html')
