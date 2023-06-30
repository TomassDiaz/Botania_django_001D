from django.contrib import admin
from .models import Usuario, tipoUsuario, Catalogo

# Register your models here.

admin.site.register(Usuario)
admin.site.register(tipoUsuario)
admin.site.register(Catalogo)