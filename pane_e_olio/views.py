from django.shortcuts import render
from django import forms
from django.contrib.auth import authenticate


def home(request):
    # Render the "index.html" template
    return render(request, 'index.html')


def aboutus(request):

    # Render the "about-us.html" template
    return render(request, 'about-us.html')


def reserve(request):
    # Render the "reserve.html" template
    return render(request, 'reserve.html')