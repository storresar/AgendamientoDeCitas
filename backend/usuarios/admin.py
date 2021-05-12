from django.contrib import admin
from usuarios.models import usuario,tipo_usuario

# Register your models here.

@admin.register(usuario)
class usuario_admin(admin.ModelAdmin):
    pass
@admin.register(tipo_usuario)
class tipo_usuario(admin.ModelAdmin):
    pass

