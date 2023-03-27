from django.db import models

# Create your models here.


from django.contrib.auth.models import User

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    table_number = models.IntegerField()
    is_confirmed = models.BooleanField(default=False)