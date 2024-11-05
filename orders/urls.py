from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.order_display, name='order_display'),
]