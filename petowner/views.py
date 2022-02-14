# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, logout

import petowner
from pet.models import Pet
from .forms import SignUpForm, LoginForm, ProfileForm
from .models import Profile


def profile(request):
    pet_list = Pet.objects.filter(user__username=request.user.username)
    return render(request, 'petowner/profile.html', {'pets': pet_list})


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')

    return render(request, 'petowner/login_form.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']

            messages.success(request, "Kendini bize tanıttığın için teşekkürler.")
            # Below 2 lines, if you want user to get logged in
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

    else:
        user_form = SignUpForm()
        profile_form = ProfileForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,

    }
    return render(request, 'petowner/signup.html', {'user_form': user_form, 'profile_form': profile_form})



def logout_view(request):
    logout(request)
    return redirect('home')
