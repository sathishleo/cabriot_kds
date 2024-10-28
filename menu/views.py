from datetime import datetime

from django.shortcuts import render
from django.views.decorators.csrf import  csrf_exempt
# Create your views here.
from django.utils import timezone  # for current date and time management
from django.shortcuts import render
from .models import DailyDisplayAssignment, DailyDisplayMenuItem, DisplaySection, MenuItem


@csrf_exempt
def bread_display(request):
    # Mock data; replace this with your actual data source
    items =DailyDisplayMenuItem.objects.all()

    # Get current time
    # current_date = datetime.now()
    current_time = datetime.now()

    return render(request, 'bread_display.html', {
        'items': items,
        'current_date': current_time,
        'current_time': current_time,
    })
