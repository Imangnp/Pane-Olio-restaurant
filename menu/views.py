from django.shortcuts import render
from .models import MenuItem



def menu(request):
    # Divide menu Items to diffrent categories
    antipasti_items = MenuItem.objects.filter(category='antipasti')
    main_courses_items = MenuItem.objects.filter(category='main_courses')
    dessert_items = MenuItem.objects.filter(category='dessert')
    red_wine_items = MenuItem.objects.filter(category='red_wine')
    white_wine_items = MenuItem.objects.filter(category='white_wine')
    beers_items = MenuItem.objects.filter(category='beers')
    soft_drinks_items = MenuItem.objects.filter(category='soft_drinks')
    context = {
        'antipasti_items': antipasti_items,
        'main_courses_items': main_courses_items,
        'dessert_items': dessert_items,
        'red_wine_items': red_wine_items,
        'white_wine_items': white_wine_items,
        'beers_items': beers_items,
        'soft_drinks_items': soft_drinks_items,

    }
    # Pass the menu items to the template
    return render(request, 'menu.html', context)
