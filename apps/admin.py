from django.contrib import admin
from .models import usuario, libros
# Register your models here.

#admin.site.register(usuario)

#admin.site.register(libros)

@admin.register(usuario)
class usuarioadmin(admin.ModelAdmin):
    search_fields=('nombre', 'apellido')
    list_display = ('nombre', 'apellido')

@admin.register(libros)
class librosadmin(admin.ModelAdmin):
    search_fields=('titulo', 'genero')
    list_display = ('titulo', 'genero', 'paginas', 'autor')



