from django.shortcuts import render, redirect
from datetime import datetime, timedelta, time, datetime
from .models import Reservation, Table
from .forms import ReservationForm
from django.utils import timezone
from django.db.models.functions import Concat
from django.db.models import Value, Q  # Import the Value and Q classes for queries
from django.db import models



# Create your views here.



def is_table_available(people, booking_date, booking_time):
    """
    Check if a table is available for the given number of people, date and time
    """

    # Combine the booking date and time into a single datetime object
    given_date_time = datetime.combine(booking_date, datetime.strptime(booking_time, "%H:%M").time())

    # Subtract two hours from the given datetime to create a datetime object for two hours before the booking time
    two_hours_before_given_date_time = given_date_time - timedelta(hours=2)

    # Make the datetime timezone-aware, using the current timezone
    aware_given_date_time = timezone.make_aware(given_date_time, timezone.get_current_timezone())
    
    # Convert the two-hour-earlier datetime to an aware datetime object using the current timezone
    aware_two_hours_before_given_date_time = timezone.make_aware(two_hours_before_given_date_time, timezone.get_current_timezone())

    print(f"given_date_time={given_date_time}")

    # Filter tables with capacity greater than or equal to the given number of people
    table_with_ge_capacity = Table.objects.filter(capacity__gte=people)

    # Filter reservations that overlap with the given date and time
    all_reservations_same_time = Reservation.objects.annotate(datetime_string=Concat('date', Value(' '), 'time', output_field=models.CharField()))\
        .filter(
            Q(datetime_string__exact=aware_given_date_time) |
            Q(datetime_string__gte=aware_two_hours_before_given_date_time)
        )

    # Debugging: Print the number of reservations that overlap with the given date and time
    print(all_reservations_same_time.count())
    
    if table_with_ge_capacity.count() > 0:
        if all_reservations_same_time.count() == 0:
            return table_with_ge_capacity[0]
        
        # Exclude reserved tables and return the first available table
        available_tables = table_with_ge_capacity.exclude(id__in=all_reservations_same_time.values_list('table_id', flat=True)).order_by('capacity')
        if available_tables.count() == 0:
            # If all tables are reserved, return None
            return None
        
        return available_tables[0]

    # If no tables with required capacity found, return None
    return None

     


# def is_table_available(people, booking_date, booking_time):
#     # Get all tables with a capacity greater than or equal to the requested number of people
#     tables_with_ge_capacity = Table.objects.filter(capacity__gte=people)

#     # Get all reservations for the requested date and time
#     reservations_same_time = Reservation.objects.filter(date=booking_date, time=booking_time)

#     # Check which tables have already been booked for 2 hours
#     booked_tables = []
#     for reservation in reservations_same_time:
#         if (reservation.end_time - reservation.start_time).seconds // 3600 >= 2:
#             booked_tables.append(reservation.table)

#     # Iterate over all tables with sufficient capacity
#     for table in tables_with_ge_capacity:
#         if table in booked_tables:
#             continue
#         if not Reservation.objects.filter(date=booking_date, time=booking_time, table=table).exists():
#             # If the table is available, return it
#             return table

#     # If no table with sufficient capacity is available for the requested time, check if another table is available
#     for reservation in reservations_same_time:
#         if reservation.table in booked_tables:
#             continue
#         for table in tables_with_ge_capacity:
#             if table in booked_tables:
#                 continue
#             if not Reservation.objects.filter(date=booking_date, time=booking_time, table=table).exists():
#                 return table


# Handles the reservation form submission
def reservation(request):
    if request.method == 'POST':
        booking_form = ReservationForm(request.POST)
        people_count = booking_form['people'].value()
        
        """ 
        Check if the booking form is valid and retrieve the number of people, 
        booking date, and booking time if it is
        """
        if booking_form.is_valid():
            people_count = booking_form.cleaned_data['people']
            booking_date = booking_form.cleaned_data['date']
            booking_time = booking_form.cleaned_data['time']

            # Check if a table is available
            possible_table = is_table_available(people_count, booking_date, booking_time)
            if possible_table:
                # Create a new reservation and save it
                booking = booking_form.save(commit=False)
                booking.is_confirmed = True
                booking.table = possible_table
                booking.date = booking_date
                booking.save()
                return render(request, 'reserve_success.html')
            else:
                return render(request, 'reserve_failed.html')
        else:
            # if the form is not valid, display the error message and the form again
            context = {'form': booking_form}
            return render(request, 'reservation.html', context)
    else:
        context = {'form': ReservationForm()}
        # Display Reservation page
        return render(request, 'reservation.html', context)