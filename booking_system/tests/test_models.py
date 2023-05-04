from django.test import TestCase
from django.contrib.auth.models import User
from booking_system.models import Table, Reservation
from datetime import date, time


class TableTest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='respo',
            password='testpassword'
        )

        # Create some test table
        self.table1 = Table.objects.create(table_number='101', capacity=2)
        self.table2 = Table.objects.create(table_number='102', capacity=2)
        self.table3 = Table.objects.create(table_number='103', capacity=2)
        self.table4 = Table.objects.create(table_number='104', capacity=3)
        self.table5 = Table.objects.create(table_number='201', capacity=4)
        self.table6 = Table.objects.create(table_number='202', capacity=4)
        self.table7 = Table.objects.create(table_number='203', capacity=4)
        self.table8 = Table.objects.create(table_number='204', capacity=5)
        self.table9 = Table.objects.create(table_number='301', capacity=8)
        self.table10 = Table.objects.create(table_number='304', capacity=10)

    # Test if table is created successfully
    def test_table_creation(self):
        table = Table.objects.create(table_number='305', capacity=8)
        self.assertEqual(table.table_number, '305')
        self.assertEqual(table.capacity, 8)

    # Test if capacity of a Table can be updated successfully
    def test_update_table_capacity(self):
        self.table1.capacity = 3
        self.table1.save()
        self.assertEqual(self.table1.capacity, 3)

    # Test querying Tables by capacity
    def test_query_tables_by_capacity(self):
        two_capacity_tables = Table.objects.filter(capacity=2)
        self.assertEqual(len(two_capacity_tables), 3)
        for table in two_capacity_tables:
            self.assertEqual(table.capacity, 2)

    # Test deleting a Table
    def test_delete_table(self):
        table = Table.objects.get(table_number='101')
        table.delete()
        with self.assertRaises(Table.DoesNotExist):
            Table.objects.get(table_number='101')

   
    # Test if __str__ method returns the table number
    def test_table_str_method(self):
        self.assertEqual(str(self.table5), '201')


class ReservationTest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='respo', 
            password='testpassword'
        )

        # Create a test table
        self.table = Table.objects.create(
            table_number='201', 
            capacity=4
        )

        # Create a test reservation
        self.reservation = Reservation.objects.create(
            table=self.table,
            user=self.user,
            name='Chet Baker',
            email='chetbaker@example.com',
            phone='1234567890',
            date='2023-06-10',
            time=time(18, 0, 0),
            people=4,
            message='This is a test reservation'
        )

    def test_reservation_creation(self):
        # Test if reservation is created successfully
        self.assertEqual(self.reservation.table, self.table)
        self.assertEqual(self.reservation.user, self.user)
        self.assertEqual(self.reservation.name, 'Chet Baker')
        self.assertEqual(self.reservation.email, 'chetbaker@example.com')
        self.assertEqual(self.reservation.phone, '1234567890')
        self.assertEqual(str(self.reservation.date), '2023-06-10')
        self.assertEqual(self.reservation.people, 4)
        self.assertEqual(str(self.reservation.time), '18:00:00')
        self.assertEqual(self.reservation.message, 'This is a test reservation')

    def test_register_time_is_set_on_save(self):
        # Test if register_time is set on save
        reservation = Reservation.objects.create(
            table=self.table,
            user=self.user,
            name='Chet Baker',
            email='chetbaker@example.com',
            phone='1234567890',
            date='2023-06-10',
            time=time(18, 0, 0),
            people=4,
            message='This is a test reservation'
        )
        self.assertIsNotNone(reservation.register_time)

    def test_reservation_str_method(self):
        # Test if __str__ method returns the name of the reservation
        self.assertEqual(str(self.reservation), 'Chet Baker')
