# menu/admin.py

from django.contrib import admin
from .models import MenuItem, Ingredient, DisplaySection, DailyDisplayAssignment

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'name')
    search_fields = ('title', 'name')

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('title', 'name')
    search_fields = ('title', 'name')

@admin.register(DisplaySection)
class DisplaySectionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)  # Add this line to enable search functionality

@admin.register(DailyDisplayAssignment)
class DailyDisplayAssignmentAdmin(admin.ModelAdmin):
    list_display = ('date', 'meal_period', 'display_section', 'menu_item', 'quantity', 'quantity_type')
    list_filter = ('date', 'meal_period', 'display_section')
    search_fields = ('menu_item__name', 'display_section__name')
    autocomplete_fields = ['menu_item', 'display_section']
