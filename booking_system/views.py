from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta, time, datetime
from .models import Reservation, Table
from .forms import ReservationForm
from django.utils import timezone
from django.db.models.functions import Concat
from django.db.models import Value, Q  # Import Value and Q classes for queries
from django.db import models


def is_table_available(people, booking_date, booking_time):
    """
    Check if a table is available for the given number of people, date and time
    """

    # Combine the booking date and time into a single datetime object
    given_date_time = datetime.combine(
        booking_date, datetime.strptime(booking_time, "%H:%M").time())

    # Subtract two hours from the given datetime
    # to create a datetime object for two hours before the booking time
    two_hours_before_given_date_time = given_date_time - timedelta(hours=2)

    # Make the datetime timezone-aware, using the current timezone
    aware_given_date_time = timezone.make_aware(
        given_date_time, timezone.get_current_timezone())

    # Convert the two-hour-earlier datetime to an aware datetime object
    # using the current timezone
    aware_two_hours_before_given_date_time = timezone.make_aware(
        two_hours_before_given_date_time, timezone.get_current_timezone())

    print(f"given_date_time={given_date_time}")

    # Filter tables with capacity greater or equal to the given n. of people
    table_with_ge_capacity = Table.objects.filter(capacity__gte=people)

    # Filter reservations that overlap with the given date and time
    all_reservations_same_time = Reservation.objects.annotate(
        datetime_string=Concat('date', Value(' '), 'time',
                               output_field=models.CharField())
        )\
        .filter(
            Q(datetime_string__exact=aware_given_date_time) |
            Q(datetime_string__gte=aware_two_hours_before_given_date_time)
        )

    # Debugging:
    # Print the number of reservations that overlap with the given date or time
    print(all_reservations_same_time.count())

    if table_with_ge_capacity.count() > 0:
        if all_reservations_same_time.count() == 0:
            return table_with_ge_capacity[0]

        # Exclude reserved tables and return the first available table
        available_tables = table_with_ge_capacity.exclude(
            id__in=all_reservations_same_time.values_list(
                'table_id', flat=True)).order_by('capacity')
        if available_tables.count() == 0:
            # If all tables are reserved, return None
            return None

        return available_tables[0]

    # If no tables with required capacity found, return None
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
            possible_table = is_table_available(people_count,
                                                booking_date,
                                                booking_time)
            if possible_table:
                # Create a new reservation and save it
                booking = booking_form.save(commit=False)
                booking.is_confirmed = True
                booking.table = possible_table
                booking.date = booking_date
                booking.user_id = request.user.id
                booking.save()
                return render(request, 'reserve_success.html')
            else:
                return render(request, 'reserve_failed.html')
        else:
            # if the form is not valid, display the form again
            context = {'form': booking_form}
            return render(request, 'reservation.html', context)
    else:
        context = {'form': ReservationForm()}
        # Display Reservation page
        return render(request, 'reservation.html', context)


# Display my Reservation dropdown list
def list_reservations(request):

    # Render the "manage_reservations.html" template
    user_reservations = Reservation.objects.filter(user_id=request.user.id)
    context = {'user_reservations': user_reservations}
    return render(request, 'manage_reservations.html', context)


# Display my choosen Reservation details
def reservation_details(request):
    selected_reservation_id = request.POST.get('reservation_dropdown')
    # Render the "reservation_details.html" template
    reservation = Reservation.objects.get(id=selected_reservation_id)
    context = {'reservation': reservation}
    return render(request, 'reservation_details.html', context)


# Edit a reservation with the given ID.
# The user must be logged in to access this functionality.
@login_required
def edit_reservation(request, reservation_id):

    form = None
    reservation = None
    context = {}

    reservation = get_object_or_404(Reservation, id=reservation_id)
    # Check if the user has permission to access the reservation
    if reservation.user == request.user:
        if request.method == 'POST':
            form = ReservationForm(request.POST, instance=reservation)
            if form.is_valid():
                # If form is valid, save changes and redirect to success page
                form.save()
                context = {'reservation': reservation}
                return render(
                    request, 'edit_reservation_success.html', context)
        else:
            # Display the reservation details in the reservation form
            initial_data = {'time': reservation.time.strftime('%H:%M')}
            form = ReservationForm(instance=reservation, initial=initial_data)
    else:
        # redirect to the reservation form
        return redirect('booking_system:reservation')  # Adjust the URL

    return render(request, 'edit_reservation.html',
                  {'form': form, 'reservation': reservation})


# Display a confirmation page for cancelling a reservation.
# The user must be logged in to access this functionality.
@login_required
def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if reservation.user == request.user:
        cancel_reservation_msg(request, reservation_id)
    else:
        # Redirect to the reservation page
        return redirect('booking_system:reservation')  # Adjust the URL

    return render(request, 'cancel_reservation.html',
                  {'reservation': reservation})


# Delete a reservation with the given ID and display a success message
def cancel_reservation_msg(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        # If submitted, delete the reservation and redirect to the success page
        reservation.delete()
        return render(request, 'cancel_reservation_msg.html',
                      {'reservation': reservation})
    else:
        return render(request, 'cancel_reservation_msg.html',
                      {'reservation': reservation})
