from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), 
    path('projects/', views.projects, name='projects'), 
    path('projects/<int:id>/', views.project_detail, name='project_detail'), 
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:id>/', views.task_detail, name='task_detail'),
    path('signin/', views.signin, name='signin'),
    path('signup', views.signup, name='signup')
]