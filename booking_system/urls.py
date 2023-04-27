from django.urls import path
from . import views

app_name = 'booking_system'

# Define the URL patterns for the menu
urlpatterns = [
    path('', views.reservation, name='reservation'),
    path('manage_reserve/', views.manage_reserve, name='manage_reserve'),
]