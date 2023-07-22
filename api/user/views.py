import re

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout

import random
# Create your views here.


def generate_session_token(length=10):
    # Define the sequence of characters to choose from
    characters = [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]

    # Generate a random string of length 10 using the sequence
    random_string = ''.join(random.SystemRandom().choice(characters) for _ in range(10))
    return random_string


@csrf_exempt  # will be signed in from other origins
def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'Send a post request with valid parameter'})

    username = request.POST['email']
    password = request.POST['password']

# Validation
    if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", username):
        return JsonResponse({'error': 'Enter a valid email'})

    if len(password) < 6:
        return JsonResponse({'error': 'Password needs to be at least of 6 characters'})

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email=username)  # grab user model based on the email

        if user.check_password(password):
            # grab email and password
            usr_dict = UserModel.objects.filter(email=username).values().first()
            usr_dict.pop('password')  # we pop it out as we don't want it travel further in the frontend

            # if the session is running
            # user tries to log in again
            # he can
            if user.session_token != '0':
                user.session_token = '0'
                user.save()
                return JsonResponse({'error': "Previous session exists!"})

            token = generate_session_token()
            # create a property
            user.session_token = token
            user.save()
            login(request, user)
            return JsonResponse({'token': token, 'user': usr_dict})

        else:
            return JsonResponse({'error': 'Invalid password'})

    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid Email'})

