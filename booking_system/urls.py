from django.urls import path
from . import views

app_name = 'booking_system'

# Define the URL patterns for the menu
urlpatterns = [
    path('', views.reservation, name='reservation'),
    path('list_reservations/', views.list_reservations, name='list_reservations'),
    path('show_reservation_details/', views.show_reservation_details, name='show_reservation_details'),
]