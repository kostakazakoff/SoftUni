from django.shortcuts import render


def profile_register(request):
    return render(request, 'accounts/register-page.html')


def profile_login(request, pk):
    return render(request, 'accounts/login-page.html')


def profile_details(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def profile_edit(request, pk):
    return render(request, 'accounts/profile-edit-page.html')


def profile_delete(request, pk):
    return render(request, 'accounts/profile-delete-page.html')
