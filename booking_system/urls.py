from django.urls import path
from . import views

app_name = 'booking_system'

# Define the URL patterns for the menu
urlpatterns = [
    path('', views.reservation, name='reservation'),
    path('list_reservations/', views.list_reservations, name='list_reservations'),
    path('reservation_details/', views.reservation_details, name='reservation_details'),
    path('cancel_reservation/<int:reservation_id>/', views.cancel_reservation, name='cancel_reservation'),
    path('cancel_reservation_msg/<int:reservation_id>/', views.cancel_reservation_msg, name='cancel_reservation_msg'),
    path('edit_reservation/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),
    path('edit_reservation_success/', views.edit_reservation, name='edit_reservation_success')
]