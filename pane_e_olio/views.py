from django.shortcuts import render


def home(request):
    # Render the "index.html" template
    return render(request, 'index.html')

def aboutus(request):
    # Render the "about-us.html" template
    return render(request, 'about-us.html')