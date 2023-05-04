from django.test import TestCase
from menu.models import MenuItem


class MenuItemModelTest(TestCase):

    def setUp(self):
        # Create an instance of the MenuItem model with predefined values for testing
        self.menu_item = MenuItem.objects.create(
            name='Carbonara', 
            category='main_courses', 
            description='Spaghetti Carbonara', 
            price=210.00
        )

    # Test name field label is correct
    def test_name_label(self):
        menu_item = MenuItem.objects.get(id=1)
        field_label = menu_item._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    # Test category field label is correct
    def test_category_label(self):
        menu_item = MenuItem.objects.get(id=1)
        field_label = menu_item._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')

    # Test description field label is correct
    def test_description_label(self):
        menu_item = MenuItem.objects.get(id=1)
        field_label = menu_item._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    # Test price field label is correct
    def test_price_label(self):
        menu_item = MenuItem.objects.get(id=1)
        field_label = menu_item._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    # Test name field has max length of 255
    def test_name_max_length(self):
        menu_item = MenuItem.objects.get(id=1)
        max_length = menu_item._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    # Test category field has correct choices
    def test_category_choices(self):
        menu_item = MenuItem.objects.get(id=1)
        choices = menu_item._meta.get_field('category').choices
        self.assertEqual(choices, [
            ('antipasti', 'Antipasti'),
            ('main_courses', 'Main Courses'),
            ('dessert', 'Dessert'),
            ('red_wine', 'Red Wine(glass)'),
            ('white_wine', 'White Wine(glass)'),
            ('beers', 'Beers'),
            ('soft_drinks', 'Soft Drinks'),
            ('hot_drinks', 'Hot Drinks'),
        ])

    # Test __str__ method returns the name of the menu item
    def test_object_name_is_name(self):
        menu_item = MenuItem.objects.get(id=1)
        expected_object_name = f'{menu_item.name}'
        self.assertEqual(expected_object_name, str(menu_item))
    
    # Test price field has two decimal places
    def test_price_has_two_decimal_places(self):
        menu_item = MenuItem.objects.get(id=1)
        self.assertTrue(menu_item.price % 1 == 0.0 or menu_item.price % 0.01 == 0.0)
