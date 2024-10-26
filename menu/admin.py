from django.contrib import admin
from .models import DailyDisplayAssignment, DailyDisplayMenuItem, MenuItem, DisplaySection

class DailyDisplayMenuItemInline(admin.TabularInline):
    model = DailyDisplayMenuItem
    extra = 1  # Adjust the number of blank rows to display by default
    fields = ('menu_item', 'quantity', 'quantity_type')

@admin.register(DailyDisplayAssignment)
class DailyDisplayAssignmentAdmin(admin.ModelAdmin):
    inlines = [DailyDisplayMenuItemInline]
    list_display = ('date', 'meal_period', 'display_section', 'get_menu_items')  # Adjusted list_display

    def get_menu_items(self, obj):
        # Custom method to display menu items in list view
        return ", ".join([
            f"{item.menu_item.title} ({item.quantity} {item.get_quantity_type_display()})"
            for item in obj.menu_items.all()
        ])
    get_menu_items.short_description = 'Menu Items'  # Header in the admin list display

admin.site.register(MenuItem)
admin.site.register(DisplaySection)
