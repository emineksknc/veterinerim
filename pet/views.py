# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404

from petowner.models import Profile
from .models import Pet
from .forms import PetForm
from django.contrib import messages
from django.db.models import Q



# Create your views here.
def pet_index(request):
    pet_list = Pet.objects.all()
    print(pet_list)
    query = request.GET.get('q')
    if query:
        pet_list = pet_list.filter(  # Search for pet_name, petowner_name, petowner_last_name
            Q(name__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)

        ).distinct()

    paginator = Paginator(pet_list, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        pets = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pets = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pets = paginator.page(paginator.num_pages)

    return render(request, 'pet/index.html', {'pets': pets})


def pet_detail(request, id):
    pet = get_object_or_404(Pet, id=id)
    petowner_phone = get_object_or_404(Profile, id=id)
    context = {
        'pet': pet,
        'petowner_phone': petowner_phone
    }
    return render(request, 'pet/detail.html', context)


def pet_create(request):
    if not request.user.is_authenticated():
        return Http404
    form = PetForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        pet = form.save(commit=False)
        pet.user = request.user
        pet.save()
        messages.success(request, "Dostunu bize tanıttığın için teşekkürler.")
        return HttpResponseRedirect(pet.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request, 'pet/form.html', context)


def pet_update(request, id):
    if not request.user.is_authenticated():
        return Http404

    pet = get_object_or_404(Pet, id=id)
    form = PetForm(request.POST or None, request.FILES or None, instance=pet)
    if form.is_valid():
        form.save()
        messages.success(request, "Dostunun bilgilerini güncelledin!")
        return HttpResponseRedirect(pet.get_absolute_url())
    context = {
        'form': form,
    }

    return render(request, 'pet/form.html', context)


def pet_delete(request, id):
    if not request.user.is_authenticated():
        return Http404
    pet = get_object_or_404(Pet, id=id)
    pet.delete()

    return redirect('petowner:profile')
