from django.contrib import admin
from .models import Task, Project

class TaskAdmin(admin.ModelAdmin): # Clase para modificar la interfaz de Tasks en el panel de administrador
    readonly_fields = ('created', ) # Campos de la base que son de sólo lectura

# Registro de modelos en el panel de administrador
admin.site.register(Project) 
admin.site.register(Task, TaskAdmin)