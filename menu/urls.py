from django.urls import path
from . import views

app_name = 'menu'

# Define the URL patterns for the menu
urlpatterns = [
    path('', views.menu, name='menu_items'),
]
