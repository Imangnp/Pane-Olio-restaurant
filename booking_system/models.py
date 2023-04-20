from django.db import models

# Create your models here.

from django.contrib.auth.models import User




class Reservation(models.Model):
    """
    Model representing a form, which should be filled to book a table.
    """
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
