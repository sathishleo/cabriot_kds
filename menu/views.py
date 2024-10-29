from datetime import datetime

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
    # Convert date string to a date object
    selected_date = datetime.now().date()

    # Determine the current meal period (e.g., Breakfast or Lunch/Dinner)
    current_hour = now().hour

    # Fetch the display section object and menu items for the selected date, section, and meal period
    # section = get_object_or_404(DisplaySection, name=display_section)
    ids=DailyDisplayAssignment.objects.filter(date=selected_date,display_section__name__icontains=display_section)
    menu_items = DailyDisplayMenuItem.objects.filter(
        assignment__in=list(ids)
    ).select_related('menu_item')
    print(menu_items)
    display_cls=Displaysection()
    section_item=display_cls.get_displaysection(display_section)
    menu_values=display_cls.get_formatted_menu_items(menu_items)

    context = {
        'section': section_item,
        'menu_items': menu_values,
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
    return render(request, template, context)
    # return render(request, "Main.html", context)