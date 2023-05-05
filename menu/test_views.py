from django.test import TestCase
from django.urls import reverse
from .models import MenuItem


class MenuViewTest(TestCase):

    # Set up initial data for the tests
    def setUp(self):
        # Create some menu items for testing
        MenuItem.objects.create(
            name='Fritto Misto', category='antipasti', price=200.00)
        MenuItem.objects.create(
            name='Carbonara', category='main_courses', price=210.00)
        MenuItem.objects.create(
            name='Tiramisu', category='dessert', price=150.00)
        MenuItem.objects.create(
            name='Chianti Classico', category='red_wine', price=130.00)
        MenuItem.objects.create(
            name='Cecchi', category='white_wine', price=130.00)
        MenuItem.objects.create(
            name='Menabrea', category='beers', price=70.00)
        MenuItem.objects.create(
            name='Fanta', category='soft_drinks', price=40.00)
        MenuItem.objects.create(
            name='Caffe', category='hot_drinks', price=40.00)

    # Test that the status code of the menu page is 200.
    def test_menu_view_url_exists_at_desired_location(self):
        url = reverse('menu:menu_items')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # Test that the correct template is used for the menu page
    def test_menu_view_template(self):
        url = reverse('menu:menu_items')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'menu.html')

    # Test that the menu view function correctly displays antipasti items
    def test_menu_view_displays_antipasti_items(self):
        url = reverse('menu:menu_items')
        response = self.client.get(url)
        self.assertContains(response, 'Fritto Misto')
        self.assertContains(response, '200.00')

    # Test that the menu view function correctly displays main courses items
    def test_menu_view_displays_main_courses_items(self):
        url = reverse('menu:menu_items')
        response = self.client.get(url)
        self.assertContains(response, 'Carbonara')
        self.assertContains(response, '210.00')

    # Test that the menu view function correctly displays dessert items
    def test_menu_view_displays_dessert_items(self):
        url = reverse('menu:menu_items')
        response = self.client.get(url)
        self.assertContains(response, 'Tiramisu')
        self.assertContains(response, '150.00')

    # Test that the menu view function correctly displays red wine items
    def test_menu_view_displays_red_wine_items(self):
        url = reverse('menu:menu_items')
        response = self.client.get(url)
        self.assertContains(response, 'Chianti Classico')
        self.assertContains(response, '130.00')

    # Test that the menu view function correctly displays white wine items
    def test_menu_view_displays_white_wine_items(self):
        url = reverse('menu:menu_items')
        response = self.client.get(url)
        self.assertContains(response, 'Cecchi')
        self.assertContains(response, '130.00')

    # Test that the menu view function correctly displays beers items
    def test_menu_view_displays_beers_items(self):
        url = reverse('menu:menu_items')
        response = self.client.get(url)
        self.assertContains(response, 'Menabrea')
        self.assertContains(response, '70.00')

    # Test that the menu view function correctly displays soft drink items
    def test_menu_view_displays_soft_drink_items(self):
        url = reverse('menu:menu_items')
        response = self.client.get(url)
        self.assertContains(response, 'Fanta')
        self.assertContains(response, '40.00')
