from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Table, Reservation
from .forms import ReservationForm
from .views import is_table_available
from datetime import datetime, timedelta, time
from django.utils import timezone


class ReservationViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.table = Table.objects.create(table_number='201', capacity=4)
        self.date = timezone.now().date()
        self.time = timezone.now().time().strftime("%H:%M")

    # Test Reservation Form view
    def test_reservation_form_view(self):
        response = self.client.get(reverse('booking_system:reservation'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservation.html')

    # Test the reservation form submission with invalid form data
    def test_reservation_with_invalid_form_data(self):
        login = self.client.login(username='testuser', password='testpassword')
        self.assertTrue(login)

        reservation_data = {
            'name': '',
            'email': 'chetbaker@example.com',
            'phone': '+1234567890',
            'people': 4,
            'date': self.date,
            'time': self.time,
            'message': 'Test reservation message'
        }
        response = self.client.post(reverse(
            'booking_system:reservation'), reservation_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservation.html')

    def test_edit_reservation_form_submission(self):
        login = self.client.login(username='testuser', password='testpassword')
        self.assertTrue(login)
        reservation_data = {
            'name': 'Chet Baker',
            'email': 'chetbaker@example.com',
            'phone': '+1234567890',
            'people': 4,
            'date': self.date,
            'time': self.time,
            'message': 'Test reservation message'
        }
        response = self.client.post(reverse(
            'booking_system:reservation'), reservation_data)
        self.assertEqual(response.status_code, 200)
