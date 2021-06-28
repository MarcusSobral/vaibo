from django.contrib import admin

from .models import Smartphone, Usuarios


@admin.register(Smartphone)
class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ('release_date', 'name', 'maker', 'display_size_pixels', 'storage', 'camera_pixels', 'chipset_short', 'battery_size')

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate', 'email', 'country')