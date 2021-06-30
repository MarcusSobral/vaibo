from django.contrib import admin

from .models import Produtos, Usuarios


@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('id', 'identification_released_date', 'identification_name_maker', 'identification_name')


@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthdate', 'email', 'country')
