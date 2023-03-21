from django.contrib import admin
from .models import MenuItem
from .models import WineList

# Register your models here.

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'description')
    list_filter = ('category',)
    search_fields = ('name', 'description')

    # def get_fields(self, request, obj=None):
    #     fields = super().get_fields(request, obj=obj)
    #     if obj and obj.category not in ('red_wine', 'white_wine'):
    #         fields.remove('price_per_glass')
    #         fields.remove('price_per_bottle')
    #     return fields

@admin.register(WineList)
class WineListAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price_per_glass', 'price_per_bottle', 'description')
    list_filter = ('category',)
    search_fields = ('name', 'category')

