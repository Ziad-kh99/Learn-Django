from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.projects, name='projects'),
    path('single-project/<str:pk>/', views.project, name='project'), 
    path('addproject/', views.createProject, name='create-project'),
    path('updateproject/<str:pk>/', views.updateProject, name='update-project'),
    path('deleteproject/<str:pk>/', views.deleteProject, name='delete-project'),
]