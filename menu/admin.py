from django.contrib import admin
from .models import MenuItem



# Admin configuration for the 'MenuItem' model.
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'description')
    list_filter = ('category',)
    search_fields = ('name', 'description')
