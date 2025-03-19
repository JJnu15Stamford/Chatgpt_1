
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('playground/', ('playground.urls')),
    path ('_debug_/', ('debug_toolbar.urls')),
]
