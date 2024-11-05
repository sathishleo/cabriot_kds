from django.shortcuts import render
from .models import Order

def order_display(request):
    # Logic to filter and display orders
    return render(request, 'orders_display.html', {'orders': Order.objects.all()})