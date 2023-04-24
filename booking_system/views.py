from django.shortcuts import render, redirect
from datetime import datetime, timedelta, time, datetime
from .models import Reservation, Table
from .forms import ReservationForm


# Create your views here.

# Checks if a table is available for a given number of people, date, time
# def is_table_available(people, booking_date, booking_time):
#     """
#     Check if a table is available for the given number of people
#     """
#     table_with_ge_capacity = Table.objects.filter(capacity__gte=people)
#     all_reservations_same_time = Reservation.objects.filter(date=booking_date).filter(time=booking_time).filter(people=people)
    
#     if len(table_with_ge_capacity) > 0:
#         if len(all_reservations_same_time) == 0:
#             return table_with_ge_capacity[0]

#         for each_table in table_with_ge_capacity:
#             for each_reservation in all_reservations_same_time:
#                 print(each_table.table_number, each_reservation.table.table_number)
#                 if each_table.table_number != each_reservation.table.table_number:
#                     return each_table
#     return None




def is_table_available(people, booking_date, booking_time):
    # Get all tables with a capacity greater than or equal to the requested number of people
    tables_with_ge_capacity = Table.objects.filter(capacity__gte=people)

    # Get all reservations for the requested date and time, and number of people
    reservations_same_time = Reservation.objects.filter(date=booking_date, time=booking_time, people=people)

    # Iterate over all tables with sufficient capacity
    for table in tables_with_ge_capacity:
        # Check if the table is available for the requested date and time
        if not Reservation.objects.filter(date=booking_date, time=booking_time, table=table).exists():
            # If the table is available, return it
            return table

    # If no table with sufficient capacity is available for the requested time, check if another table is available
    for reservation in reservations_same_time:
        for table in tables_with_ge_capacity:
            if not Reservation.objects.filter(date=booking_date, time=booking_time, table=table).exists():
                return table

    # If no table is available, return None
    return None


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