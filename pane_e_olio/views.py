from django.shortcuts import render


def home(request):
    # Render the "index.html" template
    return render(request, 'index.html')

