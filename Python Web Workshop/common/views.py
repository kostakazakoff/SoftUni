from django.shortcuts import render, redirect
from photos.models import Photo
from .models import PhotoLike

def home_view(request):
    context = {
        'all_photos': Photo.objects.all(),
    }
    print(context)
    return render(request, 'common/home-page.html', context)

def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = PhotoLike.objects.filter(to_photo_id=photo.id).first()

    if liked_object:
        liked_object.delete()
    else:
        new_liked_object = PhotoLike(to_photo=photo)
        new_liked_object.save()
    

    return redirect(request.META.get('HTTP_REFERER') + f'#photo-{photo_id}')
