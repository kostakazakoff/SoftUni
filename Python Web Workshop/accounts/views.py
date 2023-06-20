from django.shortcuts import render


def profile_register(request):
    return render(request, 'register.html')


def profile_login(request):
    return render(request, 'login-page.html')


def profile_details(request):
    return render(request, 'profile-details-page.html')


def profile_edit(request):
    return render(request, 'profile-edit-page.html')


def profile_delete(request):
    return render(request, 'profile-delete-page.html')
