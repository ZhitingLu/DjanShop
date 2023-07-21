from django.shortcuts import render

import random
# Create your views here.


def generate_session_token(length=10):
    # Define the sequence of characters to choose from
    characters = [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]

    # Generate a random string of length 10 using the sequence
    random_string = ''.join(random.SystemRandom().choice(characters) for _ in range(10))
    return random_string

