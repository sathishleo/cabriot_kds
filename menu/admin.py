from django.contrib import admin
from .models import DailyDisplayAssignment, DailyDisplayMenuItem, MenuItem, DisplaySection

class DailyDisplayMenuItemInline(admin.TabularInline):
    model = DailyDisplayMenuItem
    extra = 1
    fields = ('menu_item', 'quantity', 'quantity_type')
    autocomplete_fields = ['menu_item']

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    search_fields = ['item_name']  # Updated to match the field name in `MenuItem`

@admin.register(DailyDisplayAssignment)
class DailyDisplayAssignmentAdmin(admin.ModelAdmin):
    inlines = [DailyDisplayMenuItemInline]
    list_display = ('date', 'meal_period', 'display_section', 'get_menu_items')

    def get_menu_items(self, obj):
        return ", ".join([
            f"{item.menu_item.item_name} ({item.quantity} {item.get_quantity_type_display()})"
            for item in obj.menu_items.all()
        ])
    get_menu_items.short_description = 'Menu Items'

admin.site.register(DisplaySection)
