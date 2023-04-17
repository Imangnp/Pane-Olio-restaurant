from django.shortcuts import render
from .models import MenuItem, WineList

# Create your views here.

def menu(request):
    # Devide menu Items to diffrent categories
    antipasti_items = MenuItem.objects.filter(category='antipasti')
    main_courses_items = MenuItem.objects.filter(category='main_courses')
    dessert_items = MenuItem.objects.filter(category='dessert')
    red_wine_items = MenuItem.objects.filter(category='red_wine')
    white_wine_items = MenuItem.objects.filter(category='white_wine')
    drink_items = MenuItem.objects.exclude(category__in=['antipasti', 'main_courses', 'dessert', 'white_wine', 'red_wine'])
    context = {
        'antipasti_items': antipasti_items,
        'main_courses_items': main_courses_items,
        'dessert_items': dessert_items,
        'red_wine_items': red_wine_items,
        'white_wine_items': white_wine_items,

    }
    # Pass the menu items to the template
    return render(request, 'menu.html', context)


def wine_list(request):
    # Retrieve all wines from the database
    wines = WineList.objects.all()

    # Pass the wines to the template as a context variable
    return render(request, 'wine_list.html', {'wine_items': wines})