from django.contrib import admin
from .models import Client, Order, OrderItem

# Registering the Client model with custom admin settings
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the 'name' field in the admin list view


# Inline for OrderItem to be used in the Order admin form
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Number of empty OrderItem rows to display in the admin form


# Registering the Order model with custom admin settings
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'client', 'date', 'meal_type', 'order_status', 'total_pax_quantity')
    list_filter = ('meal_type', 'order_status', 'date')
    inlines = [OrderItemInline]  # Including the inline for OrderItems


# Registering the Shift model in the admin panel
# class ShiftInline(admin.TabularInline):
#     model = Shift  # The model being edited
#     extra = 1  # Number of empty forms displayed by default
#
# class ShiftAdmin(admin.ModelAdmin):
#     list_display = ['date', 'shift_name', 'start_time', 'end_time']  # Fields to display in the list view
#     list_filter = ['shift_name']  # Filter options for shift name
#     search_fields = ['date']  # Search by date
#     inlines = [ShiftInline]  # Display the ShiftInline in the admin
#
# admin.site.register(Shift, ShiftAdmin)

# orders/admin.py
from django.contrib import admin
from .models import Workday, UserShift

class UserShiftInline(admin.TabularInline):
    model = UserShift
    extra = 1

@admin.register(Workday)
class WorkdayAdmin(admin.ModelAdmin):
    list_display = ('date',)
    inlines = [UserShiftInline]
