from django.contrib import admin
from .models import Client, Order, OrderItem
from menu.models import MenuItem
# @admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'client_code')  # Display client_code in list view
    fields = ('name', 'client_code')  # Make client_code editable in the form view
admin.site.register(Client, ClientAdmin)
# @admin.register(MenuItem)
# class ItemAdmin(admin.ModelAdmin):
#     list_display = ('name', 'unit')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'client', 'date', 'meal_type', 'order_status', 'total_pax_quantity')
    list_filter = ('meal_type', 'order_status', 'date')
    inlines = [OrderItemInline]
