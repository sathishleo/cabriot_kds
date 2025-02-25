import json

import pytz
from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime

from django.utils import timezone
from django.utils.timezone import make_aware

# from .models import Order, OrderItem, UserShift

from django.utils.timezone import make_aware, now
from django.shortcuts import render
from datetime import datetime
import pytz

from .models import Order, OrderItem, MealTimeConfig, MealTime
from .utlis.utlis import order_class

from .utlis import utlis


def order_display(request):
#     # Set up timezone-aware current time and date
    current_datetime = make_aware(datetime.now())
    current_time = current_datetime.time().replace(second=0, microsecond=0)
    current_date = current_datetime.date()

    # Retrieve the latest Workday (if any)
    mealconfig = MealTimeConfig.objects.all()
    if not mealconfig.exists():
        return render(request, 'orders.html', {"detail": "No Workday shift found."})

    latest_workday = mealconfig.first()
    ids=latest_workday.pk

    # Get UserShifts for the latest Workday
    print(latest_workday)
    shifts_today = MealTime.objects.filter(config=latest_workday)

    # Determine the current active shift based on the time
    current_shift = None
    for shift in shifts_today:
        start_time = shift.start_time.replace(second=0, microsecond=0)
        end_time = shift.end_time.replace(second=0, microsecond=0)

        # Check if current time is within the shift time range
        # Check if the shift spans across midnight (i.e., start_time > end_time)
        if start_time <= end_time:
            # The range does not span midnight
            if start_time <= current_time <= end_time:
                current_shift = shift.name
                break
        else:
            # The range spans midnight (e.g., 20:00 to 06:00)
            if current_time >= start_time or current_time <= end_time:
                current_shift = shift.name
                break

    # If an active shift is found, retrieve and display orders
    if current_shift:
        orders_in_current_shift = Order.objects.filter(meal_type=current_shift, date=current_date).values_list("id",flat=True)
        order_object = Order.objects.filter(id__in=orders_in_current_shift).values('client__name', 'order_status', 'order_number', 'meal_type', 'total_pax_quantity','id')
        orders_data = Order.objects.filter(meal_type=current_shift, date=current_date).values()
        # order = Order.objects.get(id=orders_in_current_shift)
        # print(order)
        # print(orders_in_current_shift)
        order_items = OrderItem.objects.filter(order__in=orders_in_current_shift)

        # print(order)
        items = list(order_items.values('id', 'order_id', 'item__item_name', 'quantity', 'quantity_type'))
        # Serialize orders and items as JSON strings
        # orders_json = json.dumps(list(orders_in_current_shift))  # Only use if you need order IDs as JSON
        # order_items_json = json.dumps(list(order_items))

        # Set up timezone-aware display time
        ist_timezone = pytz.timezone('Asia/Kolkata')
        ist_now = now().astimezone(ist_timezone)
        current_display_time = ist_now.strftime("%I:%M:%S %p")
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            print("_______",{
                "meal":current_shift,
            "orders":list(order_object),
            'current_date': ist_now.date(),
            'current_time': current_display_time,
            "items_json":list(items)
            })
            return JsonResponse({
                "meal":current_shift,
            "orders":list(order_object),
            'current_date': ist_now.date(),
            'current_time': current_display_time,
            "items_json":list(items)
        }, safe=False)

        context = {
            "meal":current_shift,
            "orders":list(order_object),
            'current_date': ist_now.date(),
            'current_time': current_display_time,
            "items_json":list(items)
        }
        print(context)

        return render(request, 'base.html', context)
    else:
        return render(request, 'orders.html', {"detail": "No active shift found."})

    # Set to None, so we know if no shift is found

    # for date in workday:
    #     # Strip the shift's start and end time to hours and minutes
    #     start_time = date.start_time.replace(second=0, microsecond=0)
    #     end_time = date.end_time.replace(second=0, microsecond=0)
    #
    #     if start_time <= time <= end_time:
    #         current_shift = date.shift_name  # Assign the matched shift
    #         break  # Stop checking once we find the correct shift
    #
    # if not current_shift:
    #     return render(request, 'orders.html', {"detail": "No active shift found."})
    #
    # # Query orders for the current shift
    # orders_in_current_shift = Order.objects.filter(meal_type__icontains=current_shift,date=current_date)
    # print(orders_in_current_shift)
    #
    #
    # # Get order items for those orders
    # order_items = OrderItem.objects.filter(order__in=orders_in_current_shift)
    #
    # # Pass the orders, items, and current time to the template
    # context = {
    #     'orders': orders_in_current_shift,
    #     'current_date': now,
    #     'current_time': now,
    #     'items':order_items
    # }
    #
    # # order = {
    # #     'client': 'John Doe',
    # #     'status': 'Completed',
    # #     'meal_type': 'Lunch',
    # #     'order_number': '12345',
    # #     'order_items': [
    # #         {'item_name': 'Burger', 'quantity': 2, 'quantity_type': 'pcs'},
    # #         {'item_name': 'Fries', 'quantity': 1, 'quantity_type': 'pack'},
    # #     ],
    # #     'count': 3
    # #     }
    # return render(request, 'orderdisplay.html', order)
