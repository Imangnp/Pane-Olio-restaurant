from django.shortcuts import render
from .models import MenuItem, WineList


# Create your views here.

def menu(request):
    # Retrieve all menu items from the database
    menu_items = MenuItem.objects.all()

    # Pass the menu items to the template as a context variable
    return render(request, 'menu.html', {'menu_items': menu_items})

def wine_list(request):
    # Retrieve all wines from the database
    wines = WineList.objects.all()

    # Pass the wines to the template as a context variable
    return render(request, 'wine_list.html', {'wine_items': wines})