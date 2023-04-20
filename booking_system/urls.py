from django.urls import path
from . import views

app_name = 'booking_system'

# Define the URL patterns for the menu
urlpatterns = [
    path('', views.reservation, name='reservation'),
    path('reserve_success/', views.reserve_success, name='reserve_success'),
    path('reserve_failed/', views.reserve_failed, name='reserve_failed'),
]