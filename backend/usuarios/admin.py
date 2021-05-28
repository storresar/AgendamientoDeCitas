from django.contrib import admin
from .models import usuario,tipo_usuario,paciente, tipo_identificacion


# Register your models here.

@admin.register(usuario)
class usuario_admin(admin.ModelAdmin):
    pass
@admin.register(tipo_usuario)
class tipo_usuario(admin.ModelAdmin):
    pass
@admin.register(paciente)
class paciente_admin(admin.ModelAdmin):
    pass
@admin.register(tipo_identificacion)
class t_identificacion_admin(admin.ModelAdmin):
    pass

