from django.shortcuts import render, redirect
from .models import Profile
from .forms import CreateProfileForm, EditProfileForm
from fruitipedia.core.casche import casched_data


def create_profile(request):
    form = CreateProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        casched_data['profile'] = Profile.objects.all().first()
        return redirect('dashboard')

    context = {'form': form}
    return render(request, 'profiles/create-profile.html', context)


def details_profile(request):
    profile = casched_data['profile']
    return render(request, 'profiles/details-profile.html', {'profile': profile})


def edit_profile(request):
    profile = Profile.objects.all().first()
    form = EditProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        casched_data['profile'] = Profile.objects.all().first()
        return redirect('details profile')

    return render(request, 'profiles/edit-profile.html', {'form': form})


def delete_profile(request):
    profile = Profile.objects.all().first()
    if request.method == 'POST':
        profile.delete()
        casched_data['profile'] = None
        return redirect('index')

    return render(request, 'profiles/delete-profile.html', {'profile': profile})
