# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render
from .models import PasswordGeneration
import datetime
import random


def redirect_to_homepage(request):
    return redirect('/home/')


def homepage(request):
    return render(request, 'homepage.html')


def generate_random_password(request):
    password_generated = random.randint(0000, 9999)
    stored_in_model = PasswordGeneration.objects.create(password_unique=password_generated)
    stored_in_model.save()
    return render(request, 'profile.html', {'password': password_generated})


def delete_password_after_limited_time():
    password_object_from_model = PasswordGeneration.objects.all()
    for password_unique in password_object_from_model:
        time_object = password_unique.created_at
        time_object_tz_removed = time_object.replace(tzinfo=None)
        current_datetime = datetime.datetime.now()
        difference = current_datetime - time_object_tz_removed
        difference_in_minutes = (difference.seconds / 60)
        if difference_in_minutes > 10:
            password_unique.delete()
