from django.shortcuts import render, redirect
from .models import Fruit
from profiles.models import Profile
from .forms import CreateFruit, EditFruit, DeleteFruit
from fruitipedia.core.casche import casched_data


def index(request):
    fruits = Fruit.objects.all()
    profile = casched_data['profile']
    return render(request, 'index.html', {'fruits': fruits, 'profile': profile})


def dashboard(request):
    profile = casched_data['profile']
    fruits = Fruit.objects.all()
    context = {'profile': profile, 'fruits': fruits}
    return render(request, 'fruits/dashboard.html', context)


def create_fruit(request):
    profile = casched_data['profile']
    form = CreateFruit(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dashboard')
    
    context = {'form': form, 'profile': profile}
    return render(request, 'fruits/create-fruit.html', context)


def fruit_details(request, id):
    profile = casched_data['profile']
    fruit = Fruit.objects.get(id=id)
    context = {'fruit': fruit, 'profile': profile}
    return render(request, 'fruits/details-fruit.html', context)


def edit_fruit(request, id):
    profile = casched_data['profile']
    fruit = Fruit.objects.get(id=id)
    form = EditFruit(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    
    context = {'form': form, 'profile': profile, 'fruit': fruit}

    return render(request, 'fruits/edit-fruit.html', context)


def delete_fruit(request, id):
    profile = casched_data['profile']
    fruit = Fruit.objects.get(id=id)
    form = DeleteFruit(request.POST or None, instance=fruit)
    if form.is_valid():
        fruit.delete()
        return redirect('dashboard')
    
    context = {'profile': profile, 'form': form, 'fruit':fruit}

    return render(request, 'fruits/delete-fruit.html', context)
