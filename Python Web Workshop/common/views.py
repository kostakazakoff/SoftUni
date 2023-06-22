from django.shortcuts import render, redirect, resolve_url
from .models import Photo, Like
from pyperclip import copy


def home(request):
    photos = Photo.objects.all()
    context = {'photos': photos}
    return render(request, 'common/home-page.html', context)


def like_functionality(request, id):
    Like.objects.create(to_photo_id=id)
    likes = Like.objects.filter(to_photo_id=id)
    if likes.count() > 1:
        [like.delete() for like in likes]


    return redirect(request.META['HTTP_REFERER'] + f'#photo-{id}')


def share_functionality(request, id):
    copy(request.META['HTTP_HOST'] + resolve_url('photo details', id))
    return redirect(request.META['HTTP_REFERER'] + f'#photo-{id}')
