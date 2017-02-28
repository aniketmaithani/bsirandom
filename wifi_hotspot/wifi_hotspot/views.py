from django.views.generic import View
from django.shortcuts import redirect, render, render_to_response
import random


def redirect_to_homepage(request):
    return redirect('/home/')


def homepage(request):
    return render(request, 'homepage.html')


def generate_random_password(request):
    password_generated = random.randint(12830912, 12312378945)
    random_string = ['#', '@', '^', '*', '!', '(', '<']
    for string in random_string:
        temp_string = random_string[random.randint(0, 6)]

    concatednated_string = str(password_generated) + temp_string
    return render(request, 'profile.html', {'password': concatednated_string})
