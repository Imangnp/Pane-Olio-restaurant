from django.contrib import admin
from .models import Reservation, Table


# Define a custom admin class for the Reservation model
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'id')

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Table)
