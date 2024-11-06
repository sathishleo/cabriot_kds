from django.shortcuts import render
from datetime import datetime
from .models import Shift, Order, OrderItem

def order_display(request):
    # Get current time
    now = datetime.now()
    current_time = now.time()
    time = current_time.replace(second=0, microsecond=0)

    # Find the current shift
    shifts = Shift.objects.all()
    current_shift = None  # Set to None, so we know if no shift is found

    for shift in shifts:
        # Strip the shift's start and end time to hours and minutes
        start_time = shift.start_time.replace(second=0, microsecond=0)
        end_time = shift.end_time.replace(second=0, microsecond=0)

        if start_time <= time <= end_time:
            current_shift = shift.shift_name  # Assign the matched shift
            break  # Stop checking once we find the correct shift

    if not current_shift:
        return render(request, 'orders.html', {"detail": "No active shift found."})

    # Query orders for the current shift
    orders_in_current_shift = Order.objects.filter(meal_type__icontains=current_shift)
    print(orders_in_current_shift)


    # Get order items for those orders
    order_items = OrderItem.objects.filter(order__in=orders_in_current_shift)

    # Pass the orders, items, and current time to the template
    context = {
        'orders': orders_in_current_shift,
        'current_date': now,
        'current_time': now,
        'items':order_items
    }

    return render(request, 'orderdisplay.html', context)
