from django.shortcuts import render
from .models import Reservation, Table
from .forms import ReservationForm


# Create your views here.




def is_table_available(date, time, people):
    """
    Check if a table is available for the given number of people
    """
    if table_number == '101':
        return people_count <= 3
    elif table_number == '102':
        return people_count <= 2
    elif table_number == '103':
        return people_count <= 2
    elif table_number == '104':
        return people_count <= 2
    elif table_number == '201':
        return people_count <= 5
    elif table_number == '202':
        return people_count <= 4
    elif table_number == '203':
        return people_count <= 4
    elif table_number == '204':
        return people_count <= 4
    else:
        return False


def reservation(request):
    if request.method == 'POST':
        booking_form = ReservationForm(request.POST)
        if booking_form.is_valid():
            table_number = booking_form.cleaned_data['table_number']
            people_count = booking_form.cleaned_data['people']
            # Check if a table is available
            if is_table_available(table_number, people_count):
                booking = booking_form.save(commit=False)
                booking.is_confirmed = True
                booking.save()
                return redirect('reserve_success')
            else:
                return redirect('reserve_failed')
    else:
        form = ReservationForm()

    context = {'form': form}
    # Display Reservation page
    return render(request, 'reservation.html', context)


def reserve_success(request):

    return render(request, 'reserve_success.html')

def reserve_failed(request):

    return render(request, 'reserve_failed.html')