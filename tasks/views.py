from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Project, Task # M O D E L O S 

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'pages/about.html')

def projects(request): # Renderiza proyectos
    projects = Project.objects.filter(user=request.user) # Filtrando sólo los proyectos que pertenecen al usuario que los creo
    return render(request, 'pages/projects/projects.html', { # Renderizado de la página donde se van a mostrar los proyectos
        'projects': projects # Se le pasan los proyectos del usuario a la plantilla para que acceda a ellos y los muestre
    })

def project_detail(request, id): # Renderiza un proyecto por id
    project = get_object_or_404(Project, pk=id, user=request.user) # Busca el proyecto por id y usuario, si no existe da error 404
    tasks = Task.objects.filter(project_id=id) # Se obtienen las tareas relacionadas al proyecto
    return render(request, 'pages/projects/project_detail.html', { # Si sí existe lo redirige a a su propia página
        'project': project, # Se le pasan los valores que contiene el proyecto
        'tasks': tasks # Se le pasan las tareas que contiene el proyecto
    })

def tasks(request): # Renderiza las tareas 
    tasks = Task.objects.filter(project__user=request.user)  # Obtiene todas las tareas que pertenecen a los proyectos asociados al usuario autenticado
    return render(request, 'pages/tasks/tasks.html', { # Renderizado de la página donde se van a mostrar las tareas
        'tasks': tasks # Se le pasan las tareas del usuario a la plantilla para que acceda a ellas y los muestre
    })

def task_detail(request, id): # Renderiza una tarea por id
    task = get_object_or_404(Task, pk=id) # Busca la tarea por id y usuario, si no existe da error 404
    return render(request, 'pages/tasks/task_detail.html', { # Si sí existe lo redirige a a su propia página
        'task': task # Se le pasan los valores que contiene la tarea
    })

def signin(request):
    return render(request, 'auth/signin.html')

def signup(request):
    return render(request, 'auth/signup.html')