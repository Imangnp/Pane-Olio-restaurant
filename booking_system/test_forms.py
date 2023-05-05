from django.test import TestCase
from booking_system import forms
from .forms import ReservationForm
from datetime import date


class TestReservationForm(TestCase):

    def test_valid_reservation_form(self):
        # Create a dictionary with valid form data
        form_data = {
            'name': 'Chet Baker',
            'phone': '1234567890',
            'email': 'chetbaker@test.com',
            'date': str(date.today()),
            'people': '2',
            'time': '12:00',
            'message': 'Special request'
        }
        form = forms.ReservationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_reservation_form(self):
        # Create a dictionary with invalid form data
        form_data = {
            'name': '',
            'phone': '1234567890',
            'email': 'chetbaker@test.com',
            'date': '2023-07-10',
            'people': '4',
            'time': '12:30',
            'message': 'Special request' 
        }
        form = ReservationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['This field is required.'])

    def test_form_invalid_email(self):
        # Create a dictionary with invalid form data (invalid email format)
        form_data = {
            'name': 'Chet Baker',
            'phone': '1234567890',
            'email': 'chetbakertest.com',  # invalid format
            'date': '2023-05-06',
            'people': '2',
            'time': '12:30',
            'message': 'No special requests',
        }
        form = ReservationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])

    def test_phone_field_validation(self):
        form_data = {
            'name': 'Chet Baker',
            'phone': '1234-567-890',
            'email': 'hetbaker@test.com',
            'date': '2023-07-10',
            'people': '2',
            'time': '12:00'
        }
        form = ReservationForm(data=form_data)
        self.assertFalse(form.is_valid())