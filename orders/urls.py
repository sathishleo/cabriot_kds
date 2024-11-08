from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import order_display

urlpatterns = [
    path('', order_display, name='orders'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)