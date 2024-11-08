from django.db import models
from django.contrib.auth.models import User 

class Project(models.Model):
    # Constantes con los valores que va almacenar la base de datos
    FRONTEND = 'F' 
    BACKEND = 'B' 
    OTHER = 'O'
    
    # Lista de elecciones de área
    AREA_CHOICES = [ # Los valores de las tuplas muestran el nombre en la interfaz
        (FRONTEND, 'Frontend'),
        (BACKEND, 'Backend'), 
        (OTHER, 'Otro')
    ]

    # Atributos de la clase
    name = models.CharField(max_length=200) # Nombre del proyecto
    description = models.TextField(blank=True, null=True) # Descripción del proyecto
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Usuario al que se va a relacionar el proyecto
    area = models.CharField( # Área del proyecto
        max_length=1, # Longitud del valor
        choices=AREA_CHOICES, # Dropdown con la lista de áreas del proyecto
        default=OTHER # Por default es "Otro" 
    )

    def __str__(self): 
        return f'{self.name} - by {self.user.username}'
    
class Task(models.Model):
    title = models.CharField(max_length=200) # Título de la tarea
    description = models.TextField(blank=True, null=True) # Descripción de la tarea
    created = models.DateTimeField(auto_now_add=True)# Fecha de creación
    date_completed = models.DateTimeField(null=True, blank=True) # Fecha para completar la tarea
    important = models.BooleanField(default=False) # Booleano para evaluar si la tarea es importante o no (opcional)
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # Proyecto al que se va a relacionar la tarea

    def __str__(self): 
        return f'{self.title} - by {self.project.user.username}'
