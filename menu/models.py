from django.db import models

# Create your models here.

class MenuItem(models.Model):
    """
    Model representing a menu item, which can be either a food or drink item.
    """

    # Choices for the food categories of a menu item
    FOOD_CATEGORIES = [
        ('antipasti', 'Antipasti'),
        ('primi', 'Primi'),
        ('secondi', 'Secondi'),
        ('dessert', 'Dessert'),
    ]

    # Choices for the drink categories of a menu item
    DRINK_CATEGORIES = [
        ('red_wine', 'Red Wine(glass)'),
        ('white_wine', 'White Wine(glass)'),
        ('beers', 'Beers'),
        ('soft_drinks', 'Soft Drinks'),
        ('hot_drinks', 'Hot Drinks'),
    ]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=FOOD_CATEGORIES+DRINK_CATEGORIES)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    """
    Returns the name of the menu item.
    """
    def __str__(self):
        return self.name


class WineList(models.Model):
    """
    Model representing a wine list item.
    """
    WINE_CATEGORIES = [
        ('red_wine', 'Red Wine'),
        ('white_wine', 'White Wine'),
    ]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=WINE_CATEGORIES)
    description = models.TextField()
    price_per_glass = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    price_per_bottle = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name