from django.contrib import admin

# from .forms import MealtimeForm
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


#
# class MealtimeInline(admin.TabularInline):
#     model = Mealtime
#     extra = 4  # Displays four inline rows by O
#     fields = ('meal_name', 'check_in')

# from .models import   # Example of parent model

# @admin.register(Mealtime)
# class MealtimeAdmin(admin.ModelAdmin):
#     form = MealtimeForm
#     list_display = ('meal_name', 'check_in')
#     list_editable = ('check_in',)
#     list_per_page = 4
#     list_display_links = ('meal_name',)

# class MealtimeInline(admin.TabularInline):
#     model = Mealtime
#     extra = 4  # Displays four inline rows by default
#     fields = ('meal_name', 'check_in')


# @admin.register(MealSchedule)
# class MealScheduleAdmin(admin.ModelAdmin):
#     inlines = [MealtimeInline]
# from django.contrib import admin
# from .models import MealTime
#
# class MealTimeAdmin(admin.ModelAdmin):
#     class MealTimeAdmin(admin.ModelAdmin):
#         # Define fields without 'user'
#         fields = [
#             'breakfast_start_time', 'breakfast_end_time',
#             'lunch_start_time', 'lunch_end_time',
#             'tea_start_time', 'tea_end_time',
#             'snack_start_time', 'snack_end_time',
#             'dinner_start_time', 'dinner_end_time',
#         ]
#
#         # Remove 'user' from fieldsets as well
#         fieldsets = (
#             (None, {
#                 'fields': (
#                     ('breakfast_start_time', 'breakfast_end_time'),
#                     ('lunch_start_time', 'lunch_end_time'),
#                     ('tea_snack_start_time', 'tea_snack_end_time'),
#                     ('dinner_start_time', 'dinner_end_time')
#                 )
#             }),
#         )
#
#
# admin.site.register(MealTime, MealTimeAdmin)

#
# from django.contrib import admin
# from .models import MealTime
#
# class MealTimeAdmin(admin.ModelAdmin):
#     list_display = ('name', 'start_time', 'end_time')
#     ordering = ('start_time',)  # Orders by start time
#
# admin.site.register(MealTime, MealTimeAdmin)


from django.contrib import admin
from .models import MealTime, MealTimeConfig

class MealTimeInline(admin.TabularInline):
    model = MealTime
    fields = ['name', 'start_time', 'end_time']
    extra = 4  # Number of extra rows shown initially

@admin.register(MealTimeConfig)
class MealTimeConfigAdmin(admin.ModelAdmin):
    inlines = [MealTimeInline]

# Register MealTime if you want to edit entries individually as well
# admin.site.register(MealTime)
