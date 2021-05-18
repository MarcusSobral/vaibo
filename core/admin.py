from django.contrib import admin

from .models import Smartphone


@admin.register(Smartphone)
class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ('release_date', 'name', 'maker', 'display_size_pixels', 'storage', 'camera_pixels', 'chipset_short', 'batery_size')
