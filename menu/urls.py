from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from .views import bread_display,display_menu_view


urlpatterns = [
    path("",bread_display,name= 'Test'),
    path('<display_section>/',display_menu_view, name='display_menu'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)