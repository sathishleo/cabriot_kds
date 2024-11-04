import json
from datetime import datetime, timedelta

import pytz
from django.core.serializers import serialize
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe
from django.utils.timezone import now
from django.views.decorators.csrf import  csrf_exempt
# Create your views here.
from django.utils import timezone  # for current date and time management
from django.shortcuts import render
from .models import DailyDisplayAssignment, DailyDisplayMenuItem, DisplaySection, MenuItem
from .utlis.utlis import Displaysection


@csrf_exempt
def bread_display(request):
    # # Mock data; replace this with your actual data source
    # items =DailyDisplayMenuItem.objects.all()
    #
    # # Get current time
    # # current_date = datetime.now()
    # current_time = datetime.now()
    # print(items)
    return render(request, 'welcome.html',{})
#
# @csrf_exempt
# def display_menu_view(request, display_section):
#     import pytz
#
#     # Get the current time in UTC
#     utc_now = datetime.now(pytz.utc)
#     print(utc_now)
#     ist = pytz.timezone("Asia/Kolkata")
#     ist_now = utc_now.astimezone(ist)
#     print(ist_now)
#     formatted_time = ist_now.strftime("%I:%M:%S %p")
#     print("formatted_time",formatted_time)
#
#     # Convert date string to a date object
#     selected_date = datetime.now().date()
#     formatted_date = selected_date.strftime("%A, %B %d").upper()
#
#     # Determine the current meal period (e.g., Breakfast or Lunch/Dinner)
#
#     now = datetime.now()
#     hour = now.hour
#     minute = now.minute
#     print(hour)
#     print(minute)
#     meal=""
#     if (hour >= 22 and minute >= 0) or (hour <= 12 and minute >= 0):
#        textContent = "BREAKFAST / LUNCH"
#        meal = "BL"
#        if (hour >= 22 and minute >= 0):
#             selected_date += timedelta(days=1)
#     else:
#         meal = "D"
#         textContent = "DINNER"
#
#     # Fetch the display section object and menu items for the selected date, section, and meal period
#     ids = DailyDisplayAssignment.objects.filter(
#         Q(date=selected_date) &
#         Q(display_section__name__icontains=display_section) &
#         Q(meal_period__icontains=meal)
#     )
#     menu_items = DailyDisplayMenuItem.objects.filter(
#         assignment__in=list(ids)
#     ).select_related('menu_item')
#     print(menu_items)
#     display_cls=Displaysection()
#     section_item=display_cls.get_displaysection(display_section)
#     print(textContent)
#     # menu_values=display_cls.get_formatted_menu_items(menu_items)
#     # print(menu_values)
#     # for item in menu_values.get("menu_item"):
#     #     print(item.image.url)
#
#     context = {
#         "menu_items":menu_items,
#         'section': section_item,
#         'formated_date': formatted_date,
#         "formated_time":formatted_time,
#         "meal":textContent
#     }
#     if display_section.lower() == display_cls.BREAD:
#         template = "bread.html"
#     elif display_section.lower() == display_cls.VEGETABLE:
#         template = "display.html"
#     elif display_section.lower() == display_cls.MAIN:
#         template = "Main.html"
#     else:
#         template = "Main.html"  # Fallback template
#     print(template)
#     # print(menu_values[0].image.url)
#     return render(request, template, context)
    # return render(request, "Main.html", context)



#
# @csrf_exempt
# def display_menu_view(request, display_section):
#     # Set up timezone and get the current time in IST
#     ist = pytz.timezone("Asia/Kolkata")
#     utc_now = datetime.now(pytz.utc)
#     ist_now = utc_now.astimezone(ist)
#     formatted_time = ist_now.strftime("%I:%M:%S %p")
#
#     # Get the current date formatted
#     selected_date = ist_now.date()
#     formatted_date = selected_date.strftime("%A, %B %d").upper()
#
#     # Determine the current meal period
#     hour, minute = ist_now.hour, ist_now.minute
#     if (hour >= 22 and minute >= 0) or (hour < 12):
#         text_content = "BREAKFAST / LUNCH"
#         meal = "BL"
#         if hour >= 22:
#             selected_date += timedelta(days=1)  # Move to the next day for late-night meals
#     else:
#         meal = "D"
#         text_content = "DINNER"
#
#     # Fetch display section and menu items for the selected date, section, and meal period
#     ids = DailyDisplayAssignment.objects.filter(
#         date=selected_date,
#         display_section__name__icontains=display_section,
#         meal_period__icontains=meal
#     )
#     menu_items_qs = DailyDisplayMenuItem.objects.filter(
#         assignment__in=ids
#     ).select_related('menu_item')
#
#     # Convert `menu_items_qs` to a JSON-serializable list
#     menu_items_json = serialize('json', menu_items_qs)
#
#     # Get the display section item
#     display_cls = Displaysection()
#     section_item = display_cls.get_displaysection(display_section)
#
#     # Prepare the context
#     context = {
#         "menu_items_json": menu_items_json,  # JSON-serializable list of dictionaries
#         'section': section_item,
#         'formatted_date': formatted_date,
#         "formatted_time": formatted_time,
#         "meal": text_content
#     }
#
#     # Choose the correct template based on the display section
#     template_map = {
#         display_cls.BREAD.lower(): "bread.html",
#         display_cls.VEGETABLE.lower(): "display.html",
#         display_cls.MAIN.lower(): "Main.html"
#     }
#     template = template_map.get(display_section.lower(), "Main.html")
#
#     return render(request, template, context)
#
# from django.core.serializers import serialize
# from django.http import JsonResponse
# from django.shortcuts import render
# from datetime import datetime, timedelta
# import pytz
# from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def display_menu_view(request, display_section):
    # Set up timezone and get the current time in IST
    ist = pytz.timezone("Asia/Kolkata")
    utc_now = datetime.now(pytz.utc)
    ist_now = utc_now.astimezone(ist)
    formatted_time = ist_now.strftime("%I:%M:%S %p")

    # Get the current date formatted
    selected_date = ist_now.date()
    formatted_date = selected_date.strftime("%A, %B %d").upper()

    # Determine the current meal period
    hour, minute = ist_now.hour, ist_now.minute
    if (hour >= 22 and minute >= 0) or (hour >= 5 and minute >= 30 ):
        text_content = "BREAKFAST / LUNCH"
        meal = "BL"
        if hour >= 22:
            selected_date += timedelta(days=1)  # Move to the next day for late-night meals
    else:
        meal = "D"
        text_content = "DINNER"

    # Fetch display section and menu items for the selected date, section, and meal period
    ids = DailyDisplayAssignment.objects.filter(
        date=selected_date,
        display_section__name__icontains=display_section,
        meal_period__icontains=meal
    )
    menu_items = DailyDisplayMenuItem.objects.filter(
        assignment__in=ids
    ).select_related('menu_item')
    menu_items_qs = DailyDisplayMenuItem.objects.filter(
        assignment__in=ids
    ).select_related('menu_item')

    # Convert QuerySet to JSON-serializable data
    menu_items_json = serialize('json', menu_items_qs)

    # Get the display section item
    display_cls = Displaysection()
    section_item = display_cls.get_displaysection(display_section)
    template = display_cls.get_template(display_section)
    menu_data = [
        {
            "item_name": item.menu_item.item_name,
            "display_name": item.menu_item.display_name,
            "quantity": item.quantity,
            "quantity_type": item.quantity_type,
            "image_url": item.menu_item.image.url if item.menu_item.image else None,
        }
        for item in menu_items
    ]

    # Prepare the context
    context = {
        "menu_items":menu_data,
        'section': section_item,
        'formatted_date': formatted_date,
        "formatted_time": formatted_time,
        "meal": text_content
    }
    # # print(context)

    # Check if the request is AJAX or for JSON response
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
    #     # Return JSON response for AJAX request
        return JsonResponse({
            "menu_items": menu_items_json,
            "formatted_date": formatted_date,
            "formatted_time": formatted_time,
            "meal": text_content,
            "section": section_item,
        },safe=False)

    # Choose the correct template based on the display section for regular HTML response
    # template_map = {
    #     display_cls.BREAD.lower(): "bread.html",
    #     display_cls.VEGETABLE.lower(): "display.html",
    #     display_cls.MAIN.lower(): "Main.html"
    # }
    # template = template_map.get(display_section.lower(), "Main.html")mp
    # con(text=json.dumps(menu_data)
    # json.dumps(context, indent=4, ensure_ascii=False)
    # print(context)
    return render(request,template,context)

@csrf_exempt
def display_items_view(request, display_section):
    # Set up timezone and get the current time in IST
    ist = pytz.timezone("Asia/Kolkata")
    utc_now = datetime.now(pytz.utc)
    ist_now = utc_now.astimezone(ist)
    formatted_time = ist_now.strftime("%I:%M:%S %p")

    # Get the current date formatted
    selected_date = ist_now.date()
    formatted_date = selected_date.strftime("%A, %B %d").upper()

    # Determine the current meal period
    hour, minute = ist_now.hour, ist_now.minute
    if (hour >= 22 and minute >= 0) or (hour < 12):
        text_content = "BREAKFAST / LUNCH"
        meal = "BL"
        if hour >= 22:
            selected_date += timedelta(days=1)  # Move to the next day for late-night meals
    else:
        meal = "D"
        text_content = "DINNER"

    # Fetch display section and menu items for the selected date, section, and meal period
    ids = DailyDisplayAssignment.objects.filter(
        date=selected_date,
        display_section__name__icontains=display_section,
        meal_period__icontains=meal
    )
    menu_items = DailyDisplayMenuItem.objects.filter(
        assignment__in=ids
    ).select_related('menu_item')
    menu_items_qs = DailyDisplayMenuItem.objects.filter(
        assignment__in=ids
    ).select_related('menu_item')
    display_cls = Displaysection()
    section_item = display_cls.get_displaysection(display_section)

    # Convert QuerySet to JSON-serializable data
    menu_items_json = serialize('json', menu_items_qs)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Return JSON response for AJAX request
        return JsonResponse({
            "menu_items": menu_items_json,
            "formatted_date": formatted_date,
            "formatted_time": formatted_time,
            "meal": text_content,
            "section": section_item,
        })
    return JsonResponse({
            "menu_items": menu_items_json,
            "formatted_date": formatted_date,
            "formatted_time": formatted_time,
            "meal": text_content,
            "section": section_item,
        })
