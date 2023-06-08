from django.shortcuts import render, redirect, resolve_url
from photos.models import Photo
from .models import PhotoLike
from pyperclip import copy


def home_view(request):
    context = {
        'all_photos': Photo.objects.all(),
    }
    print(context)
    return render(request, 'common/home-page.html', context)


def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = PhotoLike.objects.filter(to_photo=photo).first()

    if liked_object:
        liked_object.delete()
    else:
        new_liked_object = PhotoLike(to_photo=photo)
        new_liked_object.save()

    return redirect(request.META.get('HTTP_REFERER') + f'#photo-{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    copy(request.META.get('HTTP_HOST') + resolve_url('details photo', photo_id))

    return redirect(request.META.get('HTTP_REFERER') + f'#photo-{photo_id}')
