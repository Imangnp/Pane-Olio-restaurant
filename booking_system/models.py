from django.db import models

# Create your models here.

from django.contrib.auth.models import User





class Table(models.Model):
    TABLE_CAPACITY_CHOICES = (
        (2, '2 People'),
        (3, '3 People'),
        (4, '4 People'),
        (5, '5 People'),
    )

    table_number = models.CharField(max_length=50, unique=True)
    capacity = models.IntegerField(choices=TABLE_CAPACITY_CHOICES)

    def __str__(self):
        return self.table_number



class Reservation(models.Model):
    """
    Model representing a form, which should be filled to book a table.
    """
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    date = models.DateField()
    people = models.IntegerField()
    time = models.TimeField()


    """
    Returns the name of the booking form.
    """
    def __str__(self):
            return self.name
