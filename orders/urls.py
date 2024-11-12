from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import order_display
app_name = 'orders'
urlpatterns = [
    path('order/', order_display, name='order')



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)