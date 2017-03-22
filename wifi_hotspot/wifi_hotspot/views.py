# -*- coding: utf-8 -*-
from django.views.generic.base import View
from django.shortcuts import redirect, render
from django.db.models import Q
from .models import PasswordGeneration
import datetime
import random
import os

def redirect_to_homepage(request):
    return redirect('/profile/')

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


class GeneratePasswordView(View):

    def get(self, request):
        try:
            with open('/home/pi/bsirandom/wifi_hotspot/wifi_hotspot/scanner.txt', 'r') as f:
                z = f.read()
        except:
            z = "none"
            pass

        if z == "BARCODE DETECTED":
            password_generated = random.randint(0000, 9999)
            delete_password_after_limited_time()
            stored_in_model = PasswordGeneration.objects.create(
                password_unique=password_generated)
            stored_in_model.save()
            os.remove('/home/pi/bsirandom/wifi_hotspot/wifi_hotspot/scanner.txt')
            return render(request, 'profile.html', {'password': password_generated})
        else:
            return render(request, 'profile.html', {'password': "PASSWORD NOT GENERATED"})

    def post(self, request):
        password = request.POST['password']
        exists = PasswordGeneration.objects.filter(
            Q(password_unique__icontains=password))
        try:
            if exists.all()[0].password_unique == password:
                print(request.META.get('REMOTE_ADDR'))
                return redirect('http://www.google.co.in/')
        except:
            return redirect('/profile/')
