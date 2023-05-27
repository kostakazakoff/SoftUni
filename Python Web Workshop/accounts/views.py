from django.shortcuts import render

def register_profile(request):
    return render(request, 'accounts/register-page.html')

def login_profile(request):
    return render(request, 'accounts/login-page.html')

def delete_profile(request, pk):
    return render(request, 'accounts/profile-delete-page.html', {'pk': pk})

def details_profile(request, pk):
    return render(request, 'accounts/profile-details-page.html', {'pk': pk})

def edit_profile(request, pk):
    return render(request, 'accounts/profile-edit-page.html', {'pk': pk})
