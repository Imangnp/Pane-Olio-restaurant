from django.contrib import admin
from .models import MenuItem
from .models import WineList

# Register your models here.

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'description')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    

# @admin.register(WineList)
# class WineListAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'price_per_glass', 'price_per_bottle', 'description')
#     list_filter = ('category',)
#     search_fields = ('name', 'category')

