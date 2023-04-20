from django.shortcuts import render
from .models import Reservation
from .forms import ReservationForm


# Create your views here.



def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReservationForm()

    context = {'form': form}
    # Display Reservation page
    return render(request, 'reservation.html', context)


def reserve_success(request):

    return render(request, 'reserve_success.html')

def reserve_failed(request):

    return render(request, 'reserve_failed.html')