from datetime import datetime, timedelta

from django.db.models import Q
from django.shortcuts import render, get_object_or_404
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

@csrf_exempt
def display_menu_view(request, display_section):
    import pytz

    # Get the current time in UTC
    utc_now = datetime.now(pytz.utc)
    print(utc_now)
    ist = pytz.timezone("Asia/Kolkata")
    ist_now = utc_now.astimezone(ist)
    print(ist_now)
    formatted_time = ist_now.strftime("%I:%M:%S %p")
    print("formatted_time",formatted_time)

    # Convert date string to a date object
    selected_date = datetime.now().date()
    formatted_date = selected_date.strftime("%A, %B %d").upper()

    # Determine the current meal period (e.g., Breakfast or Lunch/Dinner)

    now = datetime.now()
    hour = now.hour
    minute = now.minute
    print(hour)
    print(minute)
    meal=""
    if (hour >= 22 and minute >= 0) or (hour <= 12 and minute >= 0):
       textContent = "BREAKFAST / LUNCH"
       meal = "BL"
       if (hour >= 22 and minute >= 0):
            selected_date += timedelta(days=1)
    else:
        meal = "D"
        textContent = "DINNER"

    # Fetch the display section object and menu items for the selected date, section, and meal period
    ids = DailyDisplayAssignment.objects.filter(
        Q(date=selected_date) &
        Q(display_section__name__icontains=display_section) &
        Q(meal_period__icontains=meal)
    )
    menu_items = DailyDisplayMenuItem.objects.filter(
        assignment__in=list(ids)
    ).select_related('menu_item')
    print(menu_items)
    display_cls=Displaysection()
    section_item=display_cls.get_displaysection(display_section)
    print(textContent)
    # menu_values=display_cls.get_formatted_menu_items(menu_items)
    # print(menu_values)
    # for item in menu_values.get("menu_item"):
    #     print(item.image.url)

    context = {
        "menu_items":menu_items,
        'section': section_item,
        'formated_date': formatted_date,
        "formated_time":formatted_time,
        "meal":textContent
    }
    if display_section.lower() == display_cls.BREAD:
        template = "bread.html"
    elif display_section.lower() == display_cls.VEGETABLE:
        template = "display.html"
    elif display_section.lower() == display_cls.MAIN:
        template = "Main.html"
    else:
        template = "Main.html"  # Fallback template
    print(template)
    # print(menu_values[0].image.url)
    return render(request, template, context)
    # return render(request, "Main.html", context)